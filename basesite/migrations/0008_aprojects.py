# Generated by Django 3.1.5 on 2021-04-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0007_remove_modeling_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprojects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
