from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from gdstorage.storage import GoogleDriveStorage

from schools.models import EducationLevel

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
    subtitle = models.CharField(
        max_length=255, default='', blank=True, null=True)
    content = RichTextField(blank=True, default='')
    image = models.ImageField(upload_to='blogposts',
                              default='', blank=True, null=True, storage=gd_storage)
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


civilities = (
    ('M.', 'M.'),
    ('Mme.', "Mme."),
    ('Mlle.', "Mlle."),
)

qualifications = (
    ('BAC', 'BAC'),
    ('BAC + 1', 'BAC + 1'),
    ('BAC + 2', 'BAC + 2'),
    ('BAC + 3', 'BAC + 3'),
    ('BAC + 4', 'BAC + 4'),
    ('BAC + 5', 'BAC + 5'),
    ('BAC + 6', 'BAC + 6'),
    ('BAC + 7', 'BAC + 7'),
)

gender_list = (
    ('M', 'Masculin'),
    ('F', 'Féminin'),
)


class Tutor(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    last_name = models.CharField(
        max_length=255, default='', blank=True, null=True)
    first_name = models.CharField(
        max_length=255, default='', blank=True, null=True)
    civility = models.CharField(max_length=50, default='', choices=civilities)
    country = CountryField(
        blank_label="", default='', blank=True, null=True)
    phone = models.CharField(max_length=255, default='',)
    qualification = models.CharField(
        max_length=50, default='BAC', choices=qualifications)
    gender = models.CharField(max_length=10, choices=gender_list)
    bio = models.TextField(default='', blank=True, null=True)
    subjects = models.ManyToManyField("Subject")
    levels = models.ManyToManyField(EducationLevel)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    experience = models.IntegerField(default='0')
    facebook_link = models.CharField(
        max_length=255, default='', blank=True, null=True)
    linkedin_link = models.CharField(
        max_length=255, default='', blank=True, null=True)
    certificate = models.ImageField(
        upload_to='tutors', default='', blank=True, null=True, storage=gd_storage)
    image = models.ImageField(
        upload_to='tutors', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.user.last_name} - {self.user.first_name}'

    def get_absolute_url(self):
        return reverse('tutor', kwargs={'pk': self.pk})


class FollowTutor(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.school}'

    def get_absolute_url(self):
        return reverse('follow_tutor', kwargs={'pk': self.pk})


class Subject(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='subjects',
                              default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subject', kwargs={'pk': self.pk})


class ForumArticle(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, default='', blank=True, null=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, default='', blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    subtitle = models.CharField(
        max_length=255, default='', blank=True, null=True)
    content = RichTextField(blank=True, default='')
    # image = models.ImageField(upload_to='blogposts', default='', blank=True, null=True, storage=gd_storage)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.last_name} - {self.title}'

    def get_absolute_url(self):
        return reverse('forum_article', kwargs={'pk': self.pk})


class Publication(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, default='', blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    subtitle = models.CharField(
        max_length=255, default='', blank=True, null=True)
    content = RichTextField(blank=True, default='')
    # image = models.ImageField(upload_to='blogposts', default='', blank=True, null=True, storage=gd_storage)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.last_name} - {self.title}'

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pk': self.pk})
