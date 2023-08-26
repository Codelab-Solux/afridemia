
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
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'content': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
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
            'subject': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'content': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
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
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'message': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'target': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
        }


class TutortForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = ('__all__')
        exclude = ('user',)
        labels = {
            'civility': 'Civilité',
            'country': 'Pays de residence',
            'tel': 'Téléphone',
            'cel': 'Cellulaire',
            'bio': 'Biographie',
            'subjects': 'Matieres',
            'grades': 'Classes',
            'years_of_experience': "Annees d'experience",
            'qualifications': 'Diplomes',
            'facebook_link': 'Lien Facebook',
            'linkedin_link': 'Lien LinkedIn',
        }
        widgets = {
            'civility': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'country': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'tel': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'cel': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            # 'address': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'bio': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'subjects': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'grades': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'years_of_experience': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'qualifications': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'facebook_link': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
            'linkedin_link': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md border-2 border-gray-200 focus:border-none focus:outline-none focus:ring focus:ring-green-300 w-full"}),
        }
