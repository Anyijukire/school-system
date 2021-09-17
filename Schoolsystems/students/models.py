from django.db import models

# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=10, help_text='eg Jane')
    last_name=models.CharField(max_length=10, help_text='eg Doe')
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField( blank=True, null=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='female' , blank=True, null=True)
    mentor=models.CharField(max_length=29, null=True, blank=True)
    medical_form=models.FileField(default='default.jpg', blank=True, null=True)
    id_number=models.CharField(max_length=20, default=5343, blank=True, null=True)
    passport_number=models.CharField(max_length=20,default=3445, blank=True, null=True)
    image=models.ImageField(upload_to='images',default='default.jpg', blank=True, null=True)
    countries=(('Uganda'),("Kenya"),('Tanzania'),('Rwanda'),('Sudan'),('South Sudan'))
    nationality=models.CharField(max_length=15, default='Ugandan', blank=True, null=True)
    class_name=models.CharField(max_length=10, null=True, blank=True)
    room_number=models.CharField(max_length=5, null=True, blank=True)
    email=models.EmailField(default='anyijukirjanett@gmail.com', blank=True, null=True)
    county_or_district=models.CharField(max_length=15, blank=True, null=True)
    big_sister=models.CharField(max_length=20, null=True, blank=True)
    
    """How django stores files"""
    def __str__(self):
       return self.first_name
    
    
