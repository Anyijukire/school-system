from . import views
from django.urls import path

urlpatterns= [
    path("cal/", views.CalendarView.as_view(), name="calendar"),
    path('list/', views.event, name='event_list'),

]
