from django.shortcuts import render
from .models import Course
from .forms import CourseForm
def register_course(request):
    if request.method =='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:    
       form=CourseForm()
    return render(request, 'register_course.html',{"form": form})

    
def course_list(request):
    coursess= Course.objects.all()
    return render(request, 'course_list.html', {'coursess':coursess})