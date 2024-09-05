import random
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
#from .models import subject
from .forms import page2_form
from .forms import page4_form
from .forms import page3_form
from polls.models import classs
from polls.models import teacher
from polls.models import sched
from polls.models import subthing1





from polls.models import nofixed

obj= nofixed()
No_fixed_real = obj.nofix 
No_fixed_real=7












dictteacher={}
days={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[]}
no_p_d=10

def index(request: HttpRequest):
    return render(request, "index.html", {"test": "this is my template"})

def index1(request):
    # this is like doing a select * from subject
    #.all makes all rows of the database into list
    '''subjectlist = subject.objects.all() 
    print(subjectlist)

    # printing out all the subjects
    for x in subjectlist:
        print(f"Subject: {x.subject} Freq: {x.frequency_s}")'''
    return render(request, "page 1.html", {"test": "this is my p1"})

def index2(request):
    return render(request, "page 2.html", {"test": "this is my p2"})

def index3(request):
    return render(request, "page 3.html", {"test": "this is my p3"})

def index4(request):
    return render(request, "page 4.html", {"test": "this is my p4"})



 
def page2(request): #for the entry blocks
    data={"form2":page2_form()}
    #print("lol")

    if request.method=="POST":
        print('ugh anirudh')
        class1=request.POST.get('grades')
        section1=request.POST.get('section')
        data={'form2':page2_form(),"grades":class1,"section":section1}
    print("lol")
    return render(request,'page 2.html',data)

def save_classinfo(request):  #to get the stuff and put it in admin
    if request.method=="POST":
        value_g=request.POST.get('grades') #from forms
        value_s=request.POST.get('section')

        datas=classs(grade=value_g,section=value_s)
        datas.save()
    return render(request,'page 2.html')


def page4(request): #this is the view
    data1={'form4':page4_form()}
    if request.method=="POST":
        
        subject1=request.POST.get('subject')
        teacher1=request.POST.get('teacher')
        data1={'form4':page4_form(),"subject":subject1,'teacher':teacher1}
        

    return render(request,'page 4.html',data1)
    
def save_teacherinfo(request): #thing to save in admin page
    
    if request.method=="POST":
        
        value_sub=request.POST.get('subject')
        value_t=request.POST.get('teacher')
        

        datas=teacher(subject=value_sub,t_name=value_t)
        datas.save()
        dictteacher[value_sub]=value_t

        

        subthing1=[]
        subthing1.append(list(dictteacher.keys()))

        print('I AM HERE')
        
        
        
        global No_fixed_real
        
        No_fixed_real=len(subthing1)
        
        print(dictteacher)

    return render(request,'page 4.html', {"sub": subthing1})



def page3(request): #this is the view
    data2={'form3':page3_form()}
    if request.method=="POST":
        
        start_time=request.POST.get('stime')
        end_time=request.POST.get('etime')
        noperiod=request.POST.get('nperiod')
        

        data2={'form3':page3_form(),'start':start_time,'end':end_time,'periodss':noperiod}

    return render(request,'page 3.html',data2)

def save_timings(request):
    global value_etime
    global value_stime
    global value_nperiod
    
    if request.method=="POST":
        value_stime=request.POST.get('stime')
        value_etime=request.POST.get('etime')
        value_nperiod=request.POST.get('nperiod')

        datas=sched(s_time=value_stime,e_time=value_etime,n_periods=value_nperiod)
        datas.save()

    return render(request,'page 3.html')
    '''def workingh(self):
         
         print('here')
         start_minutes=self.value_stime.hour*60+ self.value_stime.minute
         
         end_minutes=self.value_etime.hour*60+ self.value_etime.minute
         print((end_minutes - start_minutes) / 60)
         print(value_nperiod)

         return (end_minutes - start_minutes) / 60'''
        




# Function to generate a schedule for a day
def generate_day_schedule(request):
    #global sub
    #sub=subthing.objects.all()

    subthing_values = subthing1.objects.all()
    print(subthing_values)
    print("hellloooo")
    day = []
    remaining_periods = no_p_d - No_fixed_real

    # Ensure that each subject appears at most twice
    print(subthing1)
    subjects_for_day = []
    for _ in range(remaining_periods):
        p = random.choice(subthing1)
        subjects_for_day.append(p)

    # Randomize the fixed subjects
    fixed_subjects = list(subthing1)
    random.shuffle(fixed_subjects)

    # Add fixed subjects and remaining subjects
    day.extend(fixed_subjects)
    day.extend(subjects_for_day)

    # Check if any subject is scheduled more than twice
    while any(day.count(subject) > 2 for subject in subthing1):
        day = []
        subjects_for_day = []
        for _ in range(remaining_periods):
            p = random.choice(subthing1)
            subjects_for_day.append(p)
        fixed_subjects = list(subthing1)
        random.shuffle(fixed_subjects)
        day.extend(fixed_subjects)
        day.extend(subjects_for_day)

    return render(request,'page 4.html',day)


def printyay():
# Generate schedule for each day
    for day_name in days:
        day_schedule = generate_day_schedule()
        days[day_name] = day_schedule

    # Print the results
    for day_name, day_list in days.items():
        print(f"{day_name}: {day_list}")

    print("\nFinal Timetable:")
    for day_name, day_list in days.items():
        print(f"{day_name}: {day_list}")


        
        
    




         

