from django.urls import path
from prioritylevels import views

urlpatterns = [
    path('priority-levels/', views.PriorityLevelList.as_view()),
]