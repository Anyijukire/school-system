from rest_framework import serializers
from students.models import Students
from trainer.models import Trainer
from event_calendar.models import Event
from course.models import Course



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields = ("first_name", "last_name", "age")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields= ("first_name", "last_name", "email")   


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields= ("event_date", "event_agenda", "event_duration")  


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields= ("unit_name", "unit_code", "trainers_name")          