from django.urls import path
from .views import regester_student
urlpatterns= [
    path("regester/", regester_student, name="register_student"),
]