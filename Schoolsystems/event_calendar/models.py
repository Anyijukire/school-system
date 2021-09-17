from django.db import models
from django.db.models.fields import CharField

class Event(models.Model):
    event_date=models.DateTimeField()
    event_agenda=models.CharField(max_length=20)
    event_duration=models.DateTimeField()
    event_planner_or_organiser=models.CharField(max_length=20, blank=True, null=True)
    event_venue=models.CharField(max_length=20, help_text='eg Bool', blank=True, null=True)
    number_of_attendees=models.PositiveSmallIntegerField( blank=True, null=True)
    event_activity=CharField(max_length=20, blank=True, null=True) 
    signed_by=models.CharField(max_length=20, blank=True, null=True)
    start_time = models.DateTimeField(default='2021-07-04 00:00', blank=True, null=True)
    end_time = models.DateTimeField(default='2021-07-04 00:00', blank=True, null=True)

    def __str__(self):
        return self.event_activity