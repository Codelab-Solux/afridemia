# Generated by Django 4.1 on 2023-08-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_plan_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subjects'),
        ),
    ]
