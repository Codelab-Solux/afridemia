# Generated by Django 4.1 on 2023-09-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_tutor_subjects_tutor_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='civility',
            field=models.CharField(choices=[('Doc.', 'Docteur'), ('Ing.', 'Ingenieur'), ('Prof.', 'Proffesseur')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='title',
            field=models.CharField(choices=[('M.', 'M.'), ('Mme.', 'Mme.'), ('Mlle.', 'Mlle.')], default='', max_length=50),
        ),
    ]
