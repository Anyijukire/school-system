from django.shortcuts import render
from rest_framework import viewsets
from students.models import Students
from .serializers import StudentSerializer
from trainer.models import Trainer
from .serializers import TrainerSerializer
from event_calendar.models import Event
from .serializers import EventSerializer
from course.models import Course
from .serializers import CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer