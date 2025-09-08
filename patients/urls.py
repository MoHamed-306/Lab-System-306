from django.urls import path
from .views import patient_search

urlpatterns = [
    path('search/', patient_search, name='patient_search'),
]
