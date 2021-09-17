from django.db import models
class Trainer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField(default='myemai@gmail.com')
    bank_account_number=models.CharField(max_length=20, blank=True, null=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    profession=models.CharField(max_length=15, default='CTO', blank=True, null=True)
    company=models.CharField(max_length=15, help_text='company', blank=True, null=True)
    job_title=models.CharField(max_length=25, help_text='eg SOftware Engineer', blank=True, null=True)
    lessons_attendance=models.CharField(max_length=15,  blank=True, null=True)
    resume=models.FileField(default='Resume.pdf')
    nationality=models.CharField(max_length=15,  blank=True, null=True)
    contract=models.FileField( blank=True, null=True)
    syllabus=models.CharField(max_length=15, default='sylabus', blank=True, null=True)
    id_Number=models.CharField(max_length=20, help_text='123456', blank=True, null=True)

    def __str__(self):
       return self.first_name
    bank_account_number=models.CharField(max_length=20)

