# Generated by Django 4.1 on 2023-09-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0038_rename_follow_followschool_alter_classroom_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='xp',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='fullname',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='twitter_link',
        ),
        migrations.AddField(
            model_name='teacher',
            name='civility',
            field=models.CharField(choices=[('M.', 'M.'), ('Mme.', 'Mme.'), ('Mlle.', 'Mlle.')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='curriculum_vitae',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='levels',
            field=models.ManyToManyField(to='schools.educationlevel'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(choices=[('BAC', 'BAC'), ('BAC + 1', 'BAC + 1'), ('BAC + 2', 'BAC + 2'), ('BAC + 3', 'BAC + 3'), ('BAC + 4', 'BAC + 4'), ('BAC + 5', 'BAC + 5'), ('BAC + 6', 'BAC + 6'), ('BAC + 7', 'BAC + 7')], default='BAC', max_length=50),
        ),
    ]