# Generated by Django 3.1.5 on 2021-04-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0006_modeling_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeling',
            name='description',
        ),
    ]
