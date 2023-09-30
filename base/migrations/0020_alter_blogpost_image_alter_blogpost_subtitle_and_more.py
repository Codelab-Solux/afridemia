# Generated by Django 4.1 on 2023-09-29 13:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0019_remove_tutor_title_alter_tutor_civility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='blogposts'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='forumarticle',
            name='author',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forumarticle',
            name='subject',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subject'),
        ),
        migrations.AlterField(
            model_name='forumarticle',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='subjects'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='certificate',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='tutors'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='facebook_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='tutors'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='linkedin_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('subtitle', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FollowTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]