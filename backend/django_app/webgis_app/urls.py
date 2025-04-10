# webgis_app/urls.py
from django.urls import path
from .views import map_view

urlpatterns = [
    # The empty string '' means this route handles the base URL (relative to how it's included below)
    path('', map_view, name='map_view'),
]
