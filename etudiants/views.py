from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import EtudiantForm
from .models import Etudiant

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

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/etudiant_list.html', {'etudiants': etudiants})

def etudiant_detail(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    return render(request, 'etudiants/etudiant_detail.html', {'etudiant': etudiant})

def etudiant_update(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant mis à jour avec succès !')
            return redirect('etudiant_detail', pk=etudiant.pk)
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = EtudiantForm(instance=etudiant)
    
    return render(request, 'etudiants/etudiant_form.html', {'form': form})

def etudiant_delete(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        messages.success(request, 'Étudiant supprimé avec succès !')
        return redirect('liste_etudiants')
    
    return render(request, 'etudiants/etudiant_confirm_delete.html', {'etudiant': etudiant})