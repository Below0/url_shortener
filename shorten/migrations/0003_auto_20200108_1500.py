# Generated by Django 3.0.2 on 2020-01-08 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20200106_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='lastest_date',
            new_name='last_accessed',
        ),
    ]
