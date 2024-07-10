from django import forms

class RecipeForm(forms.Form):
    location = forms.CharField(label='Your Location', max_length=100)
