from PIL import Image
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import PositiveSmallIntegerField


# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mentor=models.CharField(max_length=29)
    medical_form=models.FileField()
    id_number=models.CharField(max_length=20)
    passport_number=models.CharField(max_length=20)
    image=models.ImageField()
    nationality=models.CharField(max_length=15)
    class_name=models.CharField(max_length=10)
    room_number=models.CharField(max_length=5)
    email=models.EmailField(default='anyijukirjanett@gmail.com')
    county_or_district=models.CharField(max_length=15)
    big_sister=models.CharField(max_length=20)
    

