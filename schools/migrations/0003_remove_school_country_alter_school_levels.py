# Generated by Django 4.2 on 2023-05-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_school_telegram_school_whatsapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='country',
        ),
        migrations.AlterField(
            model_name='school',
            name='levels',
            field=models.ManyToManyField(blank=True, to='schools.educationlevel'),
        ),
    ]
