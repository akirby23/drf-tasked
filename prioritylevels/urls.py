from django.urls import path
from prioritylevels import views

urlpatterns = [
    path('priority-levels/', views.PriorityLevelList.as_view()),
    path('priority-levels/<int:pk>/', views.PriorityLevelDetail.as_view()),
]
