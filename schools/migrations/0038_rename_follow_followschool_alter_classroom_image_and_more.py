# Generated by Django 4.1 on 2023-09-29 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0037_remove_school_quote_remove_school_success_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='FollowSchool',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/classrooms'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='serie',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.serie'),
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.serie'),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/departments'),
        ),
        migrations.AlterField(
            model_name='educationlevel',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='levels'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.FileField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/gallerie'),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='classroom',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='email',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='last_school',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, default='', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='banner',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/banners'),
        ),
        migrations.AlterField(
            model_name='school',
            name='cel',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='certificate',
            field=models.FileField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/cerificate'),
        ),
        migrations.AlterField(
            model_name='school',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='crest',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/crests'),
        ),
        migrations.AlterField(
            model_name='school',
            name='moto',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/thumbnails'),
        ),
        migrations.AlterField(
            model_name='school',
            name='website',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='schoolarticle',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/school_articles'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/structures'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='facebook_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/teachers'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='linkedin_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualifications',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='twitter_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]