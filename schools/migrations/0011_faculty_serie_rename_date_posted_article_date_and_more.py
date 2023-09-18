# Generated by Django 4.1 on 2023-08-07 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_alter_article_image_alter_structure_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date_posted',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='classroom',
            old_name='fee',
            new_name='fees',
        ),
        migrations.RenameField(
            model_name='classroom',
            old_name='info',
            new_name='overview',
        ),
        migrations.RenameField(
            model_name='preinscription',
            old_name='date_posted',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='preinscription',
            old_name='title',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='structure',
            old_name='info',
            new_name='overview',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='maxseats',
        ),
        migrations.RemoveField(
            model_name='preinscription',
            name='content',
        ),
        migrations.RemoveField(
            model_name='preinscription',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='preinscription',
            name='classroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schools.classroom'),
        ),
        migrations.AddField(
            model_name='preinscription',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='preinscription',
            name='overview',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='structure',
            name='genre',
            field=models.CharField(choices=[('canteen', 'Cantine'), ('gym', 'Espace de sport'), ('laboratory', 'Laboratoire'), ('library', 'Bibliotheque'), ('pool', 'Piscine'), ('class', 'Salle de classe'), ('playground', 'Cour de récréation'), ('infirmary', 'Infirmerie')], default='', max_length=50),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('schoolfees', models.IntegerField(blank=True, default='0', null=True)),
                ('staff_number', models.IntegerField(blank=True, default='0', null=True)),
                ('students_number', models.IntegerField(blank=True, default='0', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='schools/departments')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.serie')),
                ('school', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.serie'),
        ),
    ]
