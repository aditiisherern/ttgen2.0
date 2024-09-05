from django.db import models
import time

# class name
class subject(models.Model):
    # class field
    subject = models.CharField(max_length=50)
    frequency_s = models.IntegerField()

class sched(models.Model):
    id=models.AutoField(primary_key=True)
    s_time=models.TimeField(default="00:00") #start time
    e_time=models.TimeField(default="00:00") #end time
    n_periods=models.IntegerField() #including snacks and lunch

class teacher(models.Model):
    t_name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)


class classs(models.Model):
    grade=models.CharField(max_length=20)
    section=models.CharField(max_length=5)

class subthing1(models.Model):
    diction=models.CharField(max_length=1000)


class nofixed(models.Model):
    nofix=models.IntegerField()
#every time 
#mysite % python3 manage.py makemigrations
#mysite % python3 manage.py migrate  



   