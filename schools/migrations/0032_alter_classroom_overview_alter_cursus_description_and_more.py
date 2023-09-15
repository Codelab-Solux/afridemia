# Generated by Django 4.1 on 2023-09-14 18:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0031_alter_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='overview',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cursus',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', 'Médiocre'), ('2', 'Passable'), ('3', 'Assez bien'), ('4', 'Bien'), ('5', 'Excellente')], max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='ad_copy',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='history',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='mgt_quote',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='pedagogy',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolarticle',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='structure',
            name='overview',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]