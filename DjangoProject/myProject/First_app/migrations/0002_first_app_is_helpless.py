# Generated by Django 3.2.3 on 2021-05-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_app',
            name='is_helpless',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]