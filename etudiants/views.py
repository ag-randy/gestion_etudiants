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