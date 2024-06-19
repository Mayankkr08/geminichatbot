from django.urls import path
from home.views import home, About, ChatAPI

urlpatterns = [
    path('', home, name='home'),  # Root URL for the home app
    path('home/', home, name='home'),  # Optional: Could be redundant since the root URL serves the home view
    path('About/', About, name='About'),
    path('api/', ChatAPI, name='ChatAPI'),
]
