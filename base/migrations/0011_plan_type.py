# Generated by Django 4.1 on 2023-08-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_tutor_is_featured_tutor_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='type',
            field=models.CharField(blank=True, choices=[('school', 'Ecole'), ('tutor', 'Enseignant')], default='', max_length=50, null=True),
        ),
    ]
