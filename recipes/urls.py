from django.urls import path
from . import views

urlpatterns = [
    path('recipes/templates', views.generate_recipe, name='generate_recipe'),
]
