from django.db import models
class Course(models.Model):
    unit_name=models.CharField(max_length=15)
    unit_code=models.CharField(max_length=10)
    duration=models.DateTimeField(blank=True, null=True)
    trainers_name=models.CharField(max_length=30, blank=True, null=True)
    course_syllabus=models.CharField(max_length=30)
    course_material=models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
       return self.unit_name