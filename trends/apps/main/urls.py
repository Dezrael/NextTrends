from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('v1/add_freqs/', views.add_freqs, name='add_freqs'),
    path('v1/get_freqs/', views.GetFreqsView.as_view()),
    path('v1/get_profs/', views.GetProfessionsView.as_view()),
    path('v1/change_model', views.change_model, name='change_model')
]