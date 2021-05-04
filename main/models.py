from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    ROLES = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor')    
    )

    DEPT = (
        ('Computer Science','Computer Science'),
        ('Mechanical','Mechanical'),
        ('DS ans Algos','DS ans Algos'),
        ('Machine Learning','Machine Learning'),
        ('Auto CAD', 'Auto CAD'),
        ('Web Development','Web Development')
    )

    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE)
    role = models.CharField(max_length=10,null=True,choices = ROLES)
    dept = models.CharField(max_length=16,null=True,choices=DEPT)

    def __str__(self):
        return self.user.username


class Question(models.Model):

    askedby = models.ForeignKey(User, null=True,on_delete = models.SET_NULL,related_name='bystud')
    askedto = models.ForeignKey(User, null=True,on_delete= models.SET_NULL,related_name='byistr')
    question = models.TextField(null=True)
    answer = models.TextField(null=True,blank=True)
    answered = models.BooleanField(default=False,blank=True)
    read = models.BooleanField(default=False,blank=True)
    
    