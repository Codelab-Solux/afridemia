# Generated by Django 4.1 on 2023-08-07 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='date_posted',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='article',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_posted',
            new_name='date',
        ),
        migrations.CreateModel(
            name='ForumArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
