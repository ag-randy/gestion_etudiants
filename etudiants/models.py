from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    programme = models.CharField(max_length=150) # Nouveau champ
    remarque = models.TextField(blank=True, null=True) # Nouveau champ
    date_inscription = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"