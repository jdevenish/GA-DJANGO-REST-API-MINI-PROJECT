# Generated by Django 3.0.6 on 2020-05-05 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200505_1322'),
        ('api', '0002_remove_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='authentication.User'),
            preserve_default=False,
        ),
    ]
