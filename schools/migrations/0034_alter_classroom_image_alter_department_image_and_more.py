# Generated by Django 4.1 on 2023-09-18 16:48

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0033_alter_classroom_overview_alter_cursus_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/classrooms'),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/departments'),
        ),
        migrations.AlterField(
            model_name='educationlevel',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='levels'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/gallerie'),
        ),
        migrations.AlterField(
            model_name='school',
            name='banner',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/banners'),
        ),
        migrations.AlterField(
            model_name='school',
            name='certificate',
            field=models.FileField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/cerificate'),
        ),
        migrations.AlterField(
            model_name='school',
            name='crest',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/crests'),
        ),
        migrations.AlterField(
            model_name='school',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/thumbnails'),
        ),
        migrations.AlterField(
            model_name='schoolarticle',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/school_articles'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/structures'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='schools/teachers'),
        ),
    ]
