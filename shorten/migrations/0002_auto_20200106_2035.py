# Generated by Django 3.0.2 on 2020-01-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='URL',
            new_name='link',
        ),
    ]
