# Generated by Django 4.2 on 2023-05-30 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_rename_date_added_advert_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civility', models.CharField(choices=[('Prof.', 'Prof.'), ('Doc.', 'Doc.'), ('M.', 'M.'), ('Mme.', 'Mme'), ('Mlle.', 'Mlle')], default='', max_length=50)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('tel', models.CharField(default='', max_length=255)),
                ('cel', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('grades', models.TextField(blank=True, null=True)),
                ('years_of_experience', models.IntegerField(default='0')),
                ('qualifications', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tutors')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
