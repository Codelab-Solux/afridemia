# Generated by Django 4.2 on 2023-05-13 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civility', models.CharField(choices=[('Prof.', 'Prof.'), ('Doc.', 'Doc.'), ('M.', 'M.'), ('Mme.', 'Mme'), ('Mlle.', 'Mlle')], default='', max_length=50)),
                ('country', models.CharField(max_length=255)),
                ('tel', models.CharField(default='', max_length=255)),
                ('cel', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('address', models.CharField(default='', max_length=255)),
                ('experience', models.CharField(blank=True, max_length=4, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('years_of_experience', models.IntegerField(default='0')),
                ('qualifications', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
