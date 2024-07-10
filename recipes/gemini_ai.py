import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/cloud-natural-language']
API_KEY = os.environ.get('GEMINI_AI_API_KEY')  # Replace with actual API key

def generate_recipe(prompt):
    credentials = Credentials.from_api_key(API_KEY, SCOPES)
    service = build('language', 'v1beta1', credentials=credentials)

    document = {
        'content': prompt,
        'type': 'PLAIN_TEXT',
    }
    encoding_type = 'UTF8'

    response = service.documents().analyzeSentiment(body={'document': document}).execute()
   
    recipe_text = response.get('sentences')[0].get('text')  
    return recipe_text
