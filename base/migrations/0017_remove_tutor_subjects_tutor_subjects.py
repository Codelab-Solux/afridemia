# Generated by Django 4.1 on 2023-09-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_years_of_experience_tutor_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='subjects',
        ),
        migrations.AddField(
            model_name='tutor',
            name='subjects',
            field=models.ManyToManyField(to='base.subject'),
        ),
    ]
