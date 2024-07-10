# Gemini API Recipe and Geolocation - Lokalista

## Expected Output

The frontend prompt shall request a recipe suggestion from the Gemini API. The geolocation will get the user's location and will be used by Gemini in creating a recipe list.

## Project Structure

### Project Files

```plaintext
myproject/
├── manage.py       # Runs project commands (server, migrations, etc.)
├── myproject/
│   ├── __init__.py
│   ├── settings.py  # Main configuration file for your project (database, apps, etc.)
│   ├── urls.py      # Defines URL patterns to map requests to views
│   └── wsgi.py      # Entry point for the web server (deployment)
└── recipes/        # Your Django application for recipes
    ├── admin.py      # Optional file for admin interface configuration
    ├── apps.py       # Optional file for automatic app registration (rarely used)
    ├── migrations/   # Folder for database schema migrations
    │   └── __init__.py
    ├── models.py     # Defines data models (like Recipe) for storing information
    ├── templates/    # Holds HTML templates for dynamic content rendering
    │   └── recipes/
    │       └── generate_recipe.html  # Template for user input and recipe display
    ├── tests.py      # Optional file for unit tests of your app
    ├── views.py      # Contains view functions that handle user requests and interact with models
    └── gemini_ai.py  # Contains the authentication for Gemini API

```
## Project Execution
```plaintext 
python manage.py runserver 8080

```
## Dependencies
Make sure to install the required dependencies:

```sh
pip install django requests geopy

