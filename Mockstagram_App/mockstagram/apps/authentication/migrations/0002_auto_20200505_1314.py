# Generated by Django 3.0.6 on 2020-05-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fName',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lName',
            new_name='last_name',
        ),
    ]
