from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    context = {}
    if request.user.is_authenticated :
        if request.user.profile.role == 'Instructor':
            notifs = len(request.user.byistr.filter(answered=False))
            context['notifs'] = notifs
        else:
            notifs = len(request.user.bystud.filter(answered=True,read=False))
            context['notifs'] = notifs
    return render(request,'main/home.html',context)

def loginpage(request):
    
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        
        if user is not None:
            login(request, user)
            context = {}
            if user.profile.role == 'Instructor':
                notifs = len(user.byistr.filter(answered=False))
                context['notifs'] = notifs
            else:
                notifs = len(user.bystud.filter(answered=True,read=False))
                context['notifs'] = notifs

            return  render(request,'main/home.html',context)
        else:
            messages.info(request, 'Invalid Username or Password')
            

    return  render(request,'main/login.html') 

def logoutUser(request):
    logout(request)
    return redirect('home')    

def register(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')


    context = {'form': form}
    return render(request,'main/register.html',context)

def teachers(request):

    context = {}
    teachers = Profile.objects.filter(role='Instructor')
    notifs = len(request.user.bystud.filter(answered=True,read=False))
    context['notifs'] = notifs
    context['teachers']= teachers
    return render(request,'main/teachers.html',context)

def createquestion(request,istrid):
    context = {}
    notifs = len(request.user.bystud.filter(answered=True,read=False))
    context['notifs'] = notifs
    if request.method == 'POST':
        ques_obj = Question()
        ques_obj.askedby = request.user
        ques_obj.askedto = Profile.objects.get(id=istrid).user
        ques_obj.question = request.POST['question']
        ques_obj.save()
        return redirect('teachers')
    istrusername = Profile.objects.get(id=istrid).user.username
    context['istr']=istrusername
    return render(request,'main/createquestion.html',context)
    
        

def istrnotifs(request):
    notifs = len(request.user.byistr.filter(answered=False))
    queries = request.user.byistr.filter(answered=False)
    context = {'queries' : queries,'notifs':notifs}

    return render(request,'main/istrnotifs.html',context)

def studnotifs(request):
    notifs = len(request.user.bystud.filter(answered=True,read=False))
    answers = request.user.bystud.filter(answered = True,read  = False)
    context = {'answers' : answers,'notifs':notifs}

    return render(request,'main/studnotifs.html',context)

def myans(request):

    if request.user.profile.role == 'Instructor':
        notifs = len(request.user.byistr.filter(answered=False))
        answers = request.user.byistr.filter(answered = True)
        context = {'answers' : answers,'notifs':notifs}

        return render(request,'main/myans.html',context)
    
    else:
        notifs = len(request.user.bystud.filter(answered=True,read=False))
        answers = request.user.bystud.filter(read = True)
        context = {'answers' : answers,'notifs':notifs}

        return render(request,'main/myans.html',context)


def update_ques(request,pk):

    ques = Question.objects.get(id=pk)
    
    
    if request.method == 'POST' and request.user.profile.role == 'Instructor':
        
        ques.answer = request.POST['answer']
        ques.answered = True
        ques.save()
        return redirect('istrnotifs')
    
    if request.method == 'POST' and request.user.profile.role == 'Student':
        
        print(request.POST)
        if 'read' in request.POST.keys() :
            ques.read = request.POST['read']
            ques.save()
            return redirect('studnotifs')
        else:
            return redirect('studnotifs')

def pending(request):
    notifs = len(request.user.bystud.filter(answered=True,read=False))
    pending_ques = request.user.bystud.filter(answered=False)
    context = {'pending_ques': pending_ques,'notifs':notifs}
    return render(request,'main/pending.html',context)