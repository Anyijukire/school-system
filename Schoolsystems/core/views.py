from django.shortcuts import render
from students.models import Students
from trainer.models import Trainer
from course.models import Course
from event_calendar.models import Event

# Create your views here.
def home(request):
    studentss=Students.objects.count()
    trainers= Trainer.objects.count()
    courses=Course.objects.count()
    events= Event.objects.count()
    data= {'studentss': studentss, 'trainers': trainers, 'courses': courses, 'events':events}
    return render(request, 'home.html', data)
