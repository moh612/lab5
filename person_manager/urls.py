
from django.urls import path
from person_app import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('', views.person_list, name='person_list'),
]