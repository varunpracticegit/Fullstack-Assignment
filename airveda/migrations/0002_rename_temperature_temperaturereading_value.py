# Generated by Django 4.2.2 on 2023-11-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airveda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperaturereading',
            old_name='temperature',
            new_name='value',
        ),
    ]
