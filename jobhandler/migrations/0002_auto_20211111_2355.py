# Generated by Django 3.2.9 on 2021-11-11 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobhandler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicants',
            old_name='job_id',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='applicant_id',
            new_name='user',
        ),
    ]