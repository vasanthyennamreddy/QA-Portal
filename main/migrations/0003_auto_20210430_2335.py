# Generated by Django 3.2 on 2021-04-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dept',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical', 'Mechanical'), ('DS ans Algos', 'DS ans Algos'), ('Machine Learning', 'Machine Learning'), ('Auto CAD', 'Auto CAD'), ('Web Development', 'Web Development')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor')], max_length=10, null=True),
        ),
    ]