from django.urls import path
from .views import etudiant_create, etudiant_delete, etudiant_detail, etudiant_update, liste_etudiants

urlpatterns = [
    path('etudiant/creer/', etudiant_create, name='etudiant_create'),
    path('', liste_etudiants, name='liste_etudiants'),
    path('etudiant/<int:pk>/', etudiant_detail, name='detail_etudiant'),  # Nouvelle route pour le détail de l'étudiant
    path('etudiant/<int:pk>/modifier/', etudiant_update, name='etudiant_update'),  # Nouvelle route pour la mise à jour de l'étudiant
    path('etudiant/<int:pk>/supprimer/', etudiant_delete, name='etudiant_delete'),  # Nouvelle route pour la suppression de l'étudiant
]