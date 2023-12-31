from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser
from django_countries.fields import CountryField
# from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class EducationLevel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='levels', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('education_level', kwargs={'pk': self.pk})


class Serie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('serie', kwargs={'pk': self.pk})


infrastructures = (
    ('-----', '-----'),
    ('canteen', 'Cantine'),
    ('gym', 'Espace de sport'),
    ('laboratory', 'Laboratoire'),
    ('library', 'Bibliotheque'),
    ('pool', 'Piscine'),
    ('playground', 'Cour de récréation'),
    ('infirmary', 'Infirmerie'),
)

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

ratings_list = (
    ('1', 'Médiocre'),
    ('2', 'Passable'),
    ('3', 'Assez bien'),
    ('4', 'Bien'),
    ('5', 'Excellente'),
)


class School(models.Model):
    manager = models.OneToOneField(
        CustomUser, unique=True, on_delete=models.CASCADE)
    country = CountryField(
        blank_label="", default='', blank=True, null=True)
    moto = models.CharField(max_length=255, default='', blank=True, null=True)
    name = models.CharField(max_length=255,)
    levels = models.ManyToManyField(EducationLevel)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(
        max_length=255, default='', blank=True, null=True)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    cel = models.CharField(max_length=255, default='', blank=True, null=True)
    whatsapp = models.CharField(
        max_length=255, default='', blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)
    #
    # quote = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pedagogy = models.TextField(blank=True, null=True)
    ad_copy = models.TextField(blank=True, null=True)
    #
    resumption_date = models.DateField(blank=True, null=True)
    opening_hour = models.TimeField(blank=True, null=True)
    closing_hour = models.TimeField(blank=True, null=True)
    #
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    avg_rating = models.FloatField(default=0.0)
    # academia
    # success_rate = models.IntegerField(default='0', blank=True, null=True)
    teacher_count = models.IntegerField(default='0', blank=True, null=True)
    student_count = models.IntegerField(default='0', blank=True, null=True)
    formation_count = models.IntegerField(default='0', blank=True, null=True)

    # files
    thumbnail = models.ImageField(
        upload_to='schools/thumbnails', default='', blank=True, null=True, storage=gd_storage)
    banner = models.ImageField(
        upload_to='schools/banners', default='', blank=True, null=True, storage=gd_storage)
    crest = models.ImageField(
        upload_to='schools/crests', default='', blank=True, null=True, storage=gd_storage)
    certificate = models.FileField(
        upload_to='schools/cerificate', default='', blank=True, null=True, storage=gd_storage)
    #
    date_added = models.DateTimeField(auto_now=True)

    def update_avg_rating(self):
        reviews = self.review_set.all()
        total_ratings = sum(int(n.rating) for n in reviews)
        ratings_count = reviews.count()

        if ratings_count > 0:
            self.avg_rating = total_ratings / ratings_count
            self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school', kwargs={'pk': self.pk})


class Review(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    comment = models.TextField(
        max_length=3000, default='', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=10, choices=ratings_list)

    def __str__(self):
        return f'{self.user} - {self.school}'

    def get_absolute_url(self):
        return reverse('review', kwargs={'pk': self.pk})


class FollowSchool(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.school}'

    def get_absolute_url(self):
        return reverse('follow_school', kwargs={'pk': self.pk})


class Teacher(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    civility = models.CharField(
        max_length=50, default='', choices=civilities)
    full_name = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    levels = models.ManyToManyField(EducationLevel)
    experience = models.IntegerField(default='0')
    qualification = models.CharField(
        max_length=50, default='BAC', choices=qualifications)
    curriculum_vitae = models.TextField(default='', blank=True, null=True,)
    linkedin_link = models.CharField(
        max_length=255, default='', blank=True, null=True)
    image = models.ImageField(
        upload_to='schools/teachers', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('teacher', kwargs={'pk': self.pk})


class Advantage(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=255, default='avantage',)

    def __str__(self):
        return self.phrase

    def get_absolute_url(self):
        return reverse('advantage', kwargs={'pk': self.pk})


class Faculty(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('faculty', kwargs={'pk': self.pk})


class Cursus(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cursus', kwargs={'pk': self.pk})


class Department(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    faculty = models.ForeignKey(
        Serie, on_delete=models.CASCADE, default='', blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    schoolfees = models.IntegerField(default='0', blank=True, null=True)
    staff_number = models.IntegerField(default='0', blank=True, null=True)
    students_number = models.IntegerField(default='0', blank=True, null=True)
    image = models.ImageField(
        upload_to='schools/departments', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.name} - {self.school}'

    def get_absolute_url(self):
        return reverse('department', kwargs={'pk': self.pk})


class Classroom(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    serie = models.ForeignKey(
        Serie, on_delete=models.SET_NULL, default='', blank=True, null=True)
    name = models.CharField(max_length=255, default='')
    fees = models.IntegerField(default='0', blank=True, null=True)
    size = models.IntegerField(default='0', blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='schools/classrooms', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.name} - {self.school}'

    def get_absolute_url(self):
        return reverse('classroom', kwargs={'pk': self.pk})


class Structure(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=50, default='', choices=infrastructures)
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default='0')
    overview = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='schools/structures', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.type} {self.name} - {self.school}'

    def get_absolute_url(self):
        return reverse('structure', kwargs={'pk': self.pk})


class SchoolArticle(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    content = RichTextField(blank=True, default='')
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='schools/school_articles', default='', blank=True, null=True, storage=gd_storage)

    def __str__(self):
        return f'{self.title} - {self.school}'

    def get_absolute_url(self):
        return reverse('school_article', kwargs={'pk': self.pk})


class Gallery(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
    year = models.CharField(max_length=4, default='year')
    images = models.FileField(
        upload_to='schools/gallerie', default='', blank=True, null=True, storage=gd_storage)


class Performance(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=4)
    exam = models.CharField(max_length=255)
    candidates = models.IntegerField(default='0')
    pass_rate = models.IntegerField(default='0')
    highest = models.FloatField(default='0')
    lowest = models.FloatField(default='0')
    year = models.CharField(max_length=4, default='year')

    def __str__(self):
        return f'{self.exam} - {self.year}'

    def get_absolute_url(self):
        return reverse('performance', kwargs={'pk': self.pk})


class PreRegistration(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE)
    classroom = models.CharField(
        max_length=255, default='', blank=True, null=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=gender_list)
    last_school = models.CharField(
        max_length=255, default='', blank=True, null=True)
    email = models.CharField(max_length=255, default='', blank=True, null=True)
    phone = models.CharField(max_length=255, default='', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.school}'

    def get_absolute_url(self):
        return reverse('pre_registration', kwargs={'pk': self.pk})
