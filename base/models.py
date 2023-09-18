from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.

categories = (
    ('free', 'Gratuit'),
    ('basic', "Basique"),
    ('pro', "Professionel"),
)

durations = (
    ('undefined', 'Indéfini'),
    ('month', 'Mois'),
    ('trimester', "Trimestre"),
    ('semester', "Semestre"),
    ('year', "Année"),
)

subscription_types = (
    ('school', 'Ecole'),
    ('tutor', 'Enseignant'),
)


class Plan(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(default='0')
    type = models.CharField(max_length=50, blank=True,
                            null=True, choices=subscription_types, default='')

    def __str__(self):
        return f'{self.name}-{self.type} ({self.price})'


class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.email}-{self.plan}'


class Blogpost(models.Model):

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, default='')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, default='')
    image = models.ImageField(upload_to='blogposts', blank=True, null=True, storage=gd_storage)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', kwargs={'pk': self.pk})


advert_targets = (('schools', 'Ecoles'),
                  ('tutors', "Enseignants"),)


class Advert(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    target = models.CharField(max_length=50, blank=True,
                              null=True, choices=advert_targets, default='')
    title = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert', kwargs={'pk': self.pk})


civ_titles = (
    ('Prof.', 'Prof.'),
    ('Doc.', 'Doc.'),
    ('M.', 'M.'),
    ('Mme.', "Mme"),
    ('Mlle.', "Mlle"),
)


class Tutor(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    civility = models.CharField(max_length=50, default='', choices=civ_titles)
    country = CountryField(
        blank_label="", blank=True, null=True)
    tel = models.CharField(max_length=255, default='',)
    cel = models.CharField(max_length=255, default='', blank=True, null=True)
    # address = models.CharField(max_length=255, default='',)
    bio = models.TextField(blank=True, null=True)
    subjects = models.TextField(blank=True, null=True)
    grades = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    years_of_experience = models.IntegerField(default='0')
    qualifications = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(
        max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(
        max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='tutors', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.user.last_name} - {self.user.first_name}'

    def get_absolute_url(self):
        return reverse('tutor', kwargs={'pk': self.pk})


class Subject(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subjects', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject', kwargs={'pk': self.pk})


class ForumArticle(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, default='')
    # image = models.ImageField(upload_to='blogposts', blank=True, null=True, storage=gd_storage)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.last_name} - {self.title}'

    def get_absolute_url(self):
        return reverse('forum_article', kwargs={'pk': self.pk})
