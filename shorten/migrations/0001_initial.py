# Generated by Django 3.0.2 on 2020-01-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og', models.TextField()),
                ('result', models.CharField(max_length=8)),
                ('lastest_date', models.DateTimeField()),
            ],
        ),
    ]