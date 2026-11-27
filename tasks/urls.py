from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.get_tasks, name="get_tasks"),
]