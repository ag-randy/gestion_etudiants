# Gestion des étudiants
Application Django (CRUD complet, vues basées sur des fonctions) pour gérer une liste d'étudiants : nom, prénom, programme, remarque.

## Technologies
Python, 
Django, 
SQLite, 
Bootstrap 5.

## Fonctionnalités
| Opération | URL |
|---|---|
| Lister les étudiants | `/` |
| Afficher les détails concernant chaque étudiant | `/etudiant/<id>/` |
| Ajouter un étudiant | `/etudiant/creer/` |
| Modifier les informations dún étudiant | `/etudiant/<id>/modifier/` |
| Supprimer un étudiant| `/etudiant/<id>/supprimer/` |

## Installation
1. Cloner le dépôt GitHub

   ```bash
   git clone https://github.com/ag-randy/gestion_etudiants.git
   ```

2. Créer l'environnement virtuel

   ```bash
   python -m venv .venv
   ```

3. Activer l'environnement virtuel

   - Git Bash :
     ```bash
     source .venv/Scripts/activate
     ```

   - PowerShell :
     ```powershell
     .venv\Scripts\Activate.ps1
     ```

4. Installer les dépendances

   ```bash
   pip install -r requirements.txt
   ```


5. Lancer le serveur Django

   ```bash
   python manage.py runserver
   ```

6. Ouvrir le site dans un navigateur

   Accéder à http://127.0.0.1:8000/


## Structure

```
gestion_etudiants/
├── manage.py
├── requirements.txt
├── README.md
├── gestion_etudiants/
│   ├── settings.py
│   └── urls.py
└── etudiants/
    ├── models.py          # modèle Etudiant
    ├── forms.py           # EtudiantForm (ModelForm)
    ├── views.py           # vues CRUD
    ├── urls.py            # routes
    ├── migrations/
    └── templates/
        └── etudiants/
            ├── base.html
            ├── etudiant_list.html
            ├── etudiant_detail.html
            ├── etudiant_form.html
            └── etudiant_confirm_delete.html
```

## Auteur
GUERRIER Randy Anderson — https://github.com/ag-randy