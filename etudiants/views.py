from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EtudiantForm

# Create your views here.

def etudiant_create(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant ajouté avec succès !')
            return redirect('etudiant_create')  # Redirige vers la même page pour ajouter un autre étudiant
    else:
        form = EtudiantForm()
    
    return render(request, 'etudiants/etudiant_form.html', {'form': form})