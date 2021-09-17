
from django import forms
from .models import Trainer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden

from .forms import TrainerRegistrationForm
def register_trainer(request):
    if request.method =='POST':
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:    
       form=TrainerRegistrationForm()
    return render(request, 'register_trainer.html',{"form": form})
  
"""shows all the trainers in a table"""
def trainer_list(request):
    trainers= Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers':trainers})

def upload_pic(request):
    if request.method == 'POST':
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            m = Trainer.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')  


def edit_trainer(request, id):
    trainer= Trainer.objects.get(id=id) 
    if request.method=='POST':
        form= TrainerRegistrationForm(request.POST, instance=trainer)    
        if form.is_valid:
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainer)   

        return render(request, 'edit_trainer.html',  {'form':form}) 
    return redirect(trainer_list)    
        
def trainer_profile(request,id):
    trainer= Trainer.objects.get(id=id)
    return render(request, 'trainer_profile.html', {'trainer':trainer})   


def delete_trainer(request, id):
    trainer= Trainer.objects.get(id=id)
    trainer.delete()
    return redirect(trainer_list)

