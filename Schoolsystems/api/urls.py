from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import EventViewSet
from .views import CourseViewSet


router=routers.DefaultRouter()
router.register("students/", StudentViewSet)
router.register("trainers/", TrainerViewSet)
router.register("events/", EventViewSet)
router.register("courses/", CourseViewSet)

urlpatterns=[
    path("", include(router.urls)),
]