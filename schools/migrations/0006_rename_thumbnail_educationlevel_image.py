# Generated by Django 4.2 on 2023-05-15 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_educationlevel_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationlevel',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
