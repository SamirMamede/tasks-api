# Generated by Django 5.0.3 on 2024-05-07 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
