# Generated by Django 4.1 on 2023-09-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0035_remove_school_telegram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='mgt_quote',
            new_name='quote',
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='cel',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='levels',
            field=models.ManyToManyField(to='schools.educationlevel'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='tel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]