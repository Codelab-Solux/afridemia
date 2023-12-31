
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('__all__')
        exclude = ('manager', 'avg_rating')
        labels = {
            'country': 'Pays',
            'moto': "Slogan",
            'name': "Raison sociale",
            'levels': "Niveaux d'etude",
            'email': 'Courier Electronique',
            'website': 'Site-web',
            'address': 'Adresse',
            'tel': 'Téléphone',
            'cel': 'Cellulaire',
            'year_founded': 'Année de fondation',
            'history': 'Histoire',
            'pedagogy': "Pédagogie",
            # 'quote': 'Mot de la Direction',
            'ad_copy': "Phrase d'accueil",
            'opening_hour': "Heure d'ouverture",
            'closing_hour': "Heure de fermeture",
            'resumption_date': "Prochaine Rentrée",
            # 'success_rate': "Taux de réussite (%)",
            'teacher_count': "Effectif des enseignants",
            'student_count': "Effectif des élèves",
            'formation_count': "Nombre de cursus",
            'thumbnail': "Image d'accueil",
            'banner': "Image de page",
            'crest': "Logo de l'ecole",
            'certificate': "Agrément",
            'is_verified': "Verifié",
            'is_featured': "Vedette",
        }
        widgets = {
            'opening_hour': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'closing_hour': TimeInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'resumption_date': DateInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'moto': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            # 'quote': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'history': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'pedagogy': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'ad_copy': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'levels': forms.CheckboxSelectMultiple(attrs={'class': ""}),
            'email': forms.EmailInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'year_founded': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            # 'success_rate': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'teacher_count': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'student_count': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'formation_count': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'tel': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'cel': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'website': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'whatsapp': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = ('__all__')
        labels = {'name': "Nom de la série", }
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'description': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class ClassroomForm(forms.ModelForm):

    class Meta:
        model = Classroom
        fields = ('__all__')
        exclude = ('school',)
        labels = {
            'school': "Ecole",
            'serie': "Série",
            'name': "Nom",
            'fees': "Frais de scolarité",
            'size': "Effectif",
            'overview': "Aperçu",
        }
        widgets = {
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'serie': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'fees': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'size': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'overview': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('__all__')
        exclude = ('school',)
        labels = {
            'school': "Ecole",
            'civility': "Civilité",
            'full_name': "Nom et prenoms",
            'subjects': "Matières",
            'levels': "Niveaux",
            'experience': "Année d'experience",
            'qualification': "Diplome",
            'curriculum_vitae': "Curriculum Vitae",
            'linkedin_link': "Lien linkedin",
        }
        widgets = {
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'full_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'subjects': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'levels': forms.CheckboxSelectMultiple(attrs={'class': ""}),
            'experience': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'qualification': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'subjects': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'curriculum_vitae': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'linkedin_link': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class StructureForm(forms.ModelForm):

    class Meta:
        model = Structure
        fields = ('__all__')
        exclude = ('school',)
        labels = {
            'school': "Ecole",
            'type': "Type de structure",
            'name': "Nom",
            'capacity': "Capacité de personne",
            'overview': "Aperçu",
        }
        widgets = {
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'type': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'capacity': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'overview': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class ArticleForm(forms.ModelForm):

    class Meta:
        model = SchoolArticle
        fields = ('__all__')
        exclude = ('school', 'date',)
        labels = {
            'school': "Ecole",
            'title': 'Titre',
            'subtitle': 'Sous-titre',
            'content': 'Contenu',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'content': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('__all__')
        exclude = ('school',)
        labels = {
            'school': "Ecole",
        }
        widgets = {
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'images': forms.FileInput()
        }


class PerformanceForm(forms.ModelForm):

    class Meta:
        model = Performance
        fields = ('__all__')
        exclude = ('school',)
        labels = {
            'school': "Ecole",
            'exam': "Examen",
            'pass_rate': "Réussite (%)",
            'fail_rate': "Echecs (%)",
            'candidates': "Candidats",
            'year': "Année",
        }
        widgets = {
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'exam': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'pass_rate': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'fail_rate': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'candidates': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'year': forms.NumberInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class PreRegForm(forms.ModelForm):

    class Meta:
        model = PreRegistration
        fields = ('__all__')
        exclude = ('school', 'date', 'user',)
        labels = {
            'school': "Ecole",
            'classroom': "Classe",
            'last_name': "Nom",
            'first_name': "Prénoms",
            'comment': "Commentaire",
            'last_school': "Ancienne Ecole",
            'gender': "Sexe",
            'phone': "Téléphone",
        }
        widgets = {
            'gender': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'school': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'classroom': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'last_school': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'email': forms.EmailInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'comment': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('__all__')
        exclude = ('school', 'date', 'user',)
        labels = {
            'rating': "Note",
            'comment': "Commentaire",
        }
        widgets = {
            'rating': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full"}),
            'comment': forms.Textarea(attrs={"rows": "3", 'class': "mb-2 p-4 rounded-md border focus:border-none focus:outline-none focus:ring-1 focus:ring-green-300 w-full", "placeholder": "Ajouter un commentaire..."}),
        }
