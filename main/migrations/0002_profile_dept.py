# Generated by Django 3.2 on 2021-04-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dept',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('ME', 'Mechanical'), ('DSA', 'DS ans Algos'), ('ML', 'Machine Learning'), ('CAD', 'Auto CAD'), ('WEB', 'Web Development')], max_length=3, null=True),
        ),
    ]
