# Generated by Django 3.1.5 on 2021-04-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0004_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
