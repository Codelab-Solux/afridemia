# Generated by Django 4.1 on 2023-08-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='ad_type',
        ),
        migrations.AddField(
            model_name='advert',
            name='type',
            field=models.CharField(blank=True, choices=[('demand', 'Demande'), ('offer', 'Offre')], default='', max_length=50, null=True),
        ),
    ]
