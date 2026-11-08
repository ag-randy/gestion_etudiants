from django.urls import path
from .views import etudiant_create, etudiant_detail, liste_etudiants

urlpatterns = [
    path('etudiant/creer/', etudiant_create, name='etudiant_create'),
    path('', liste_etudiants, name='liste_etudiants'),
    path('etudiant/<int:pk>/', etudiant_detail, name='etudiant_detail'),  # Nouvelle route pour le détail de l'étudiant
]