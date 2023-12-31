# Generated by Django 4.1 on 2023-08-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0015_teacher_cv_alter_structure_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preregistration',
            name='overview',
        ),
        migrations.AddField(
            model_name='preregistration',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preregistration',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='preregistration',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], default='M', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preregistration',
            name='last_school',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preregistration',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='preregistration',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
