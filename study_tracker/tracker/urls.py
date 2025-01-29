from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('subject/<int:subject_id>/', views.unit_list, name='unit_list'),
    path('mark_completed/<int:unit_id>/', views.mark_completed, name='mark_completed'),
]