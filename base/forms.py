
from .models import *
from django import forms


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blogpost
        fields = ('__all__')
        exclude = ('author', 'date',)
        labels = {
            'title': 'Titre',
            'subtitle': 'Sous-titre',
            'content': 'Contenu',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'content': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
        }


class ForumArticleForm(forms.ModelForm):

    class Meta:
        model = ForumArticle
        fields = ('__all__')
        exclude = ('author', 'date',)
        labels = {
            'title': 'Titre',
            'subtitle': 'Sous-titre',
            'content': 'Contenu',
            'subject': 'Matière',
        }
        widgets = {
            'subject': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'content': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
        }


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('__all__')
        exclude = ('author',)
        labels = {
            'title': 'Titre',
            'target': 'Audience',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'message': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'target': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
        }


class TutortForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'last_name': 'Nom',
            'first_name': 'Prénoms',
            'civility': 'Civilité',
            'country': 'Pays de residence',
            'phone': 'Téléphone',
            'levels': 'Niveaux',
            'subjects': 'Matieres',
            'bio': 'A propos de moi',
            'experience': "Annees d'experience",
            'qualification': 'Niveau Scolaire',
            'facebook_link': 'Lien Facebook',
            'linkedin_link': 'Lien LinkedIn',
            'certificate': 'Justifs',
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'levels': forms.CheckboxSelectMultiple(attrs={'class': ""}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': ""}),
            'bio': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'experience': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'qualification': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'facebook_link': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
            'linkedin_link': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring-2 focus:ring-green-300 w-full"}),
        }
