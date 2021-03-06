# Generated by Django 2.0.2 on 2018-03-04 04:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleSlackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(0, 'Event'), (1, 'Command')])),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
