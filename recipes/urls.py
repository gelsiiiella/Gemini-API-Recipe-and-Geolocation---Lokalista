from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_recipe, name='generate_recipe'),
]
