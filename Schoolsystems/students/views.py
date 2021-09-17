from django import forms
from .models import Students
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .forms import StudentRegistrationForm
def regester_student(request):
    if request.method =='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:    
       form=StudentRegistrationForm()
    return render(request, 'register_student.html',{"form": form})
  
"""shows all the students in a table"""
def student_list(request):
    studentss= Students.objects.all()
    return render(request, 'student_list.html', {'studentss':studentss})

def upload_pic(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            m = Students.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')  


def edit_student(request, id):
    student= Students.objects.get(id=id) 
    if request.method=='POST':
        form= StudentRegistrationForm(request.POST, instance=student)    
        if form.is_valid:
            form.save()
    else:
        form=StudentRegistrationForm(instance=student)   

        return render(request, 'edit_student.html',  {'form':form}) 
    return redirect(student_list)    
def student_profile(request,id):
    student= Students.objects.get(id=id)
    return render(request, 'student_profile.html', {'student':student})   


def delete_student(request, id):
    student= Students.objects.get(id=id)
    student.delete()
    return redirect(student_list)

