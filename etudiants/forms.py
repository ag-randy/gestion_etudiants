from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'programme', 'remarque']


widgets = {
    'nom': forms.TextInput(attrs={'class': 'form-control'}),
    'prenom': forms.TextInput(attrs={'class': 'form-control'}),
    'programme': forms.TextInput(attrs={'class': 'form-control'}),
    'remarque': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
}