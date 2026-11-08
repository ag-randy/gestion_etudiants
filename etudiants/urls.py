from django.urls import path
from .views import etudiant_create

urlpatterns = [
    path('etudiant/creer/', etudiant_create, name='etudiant_create'),
]