import requests
from django.shortcuts import render
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from django.views.decorators.csrf import csrf_exempt
from .forms import RecipeForm
from django.http import HttpResponse

def root_view(request):
    return HttpResponse("Welcome to the home page!")



def root_view(request):
    return HttpResponse("Welcome to the home page!")

@csrf_exempt
def generate_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            geolocator = Nominatim(user_agent="myproject")
            loc = geolocator.geocode(location)
            latitude = loc.latitude
            longitude = loc.longitude
            

            gemini_api_url = "https://api.gemini.com/recipe-suggestions"
            params = {'latitude': latitude, 'longitude': longitude}
            response = requests.get(gemini_api_url, params=params)
            data = response.json()
            
            recipe = data.get('recipe', 'No recipe found for this location')
            return render(request, 'recipes/generate_recipe.html', {'form': form, 'recipe': recipe})
    else:
        form = RecipeForm()
    return render(request, 'recipes/generate_recipe.html', {'form': form})
