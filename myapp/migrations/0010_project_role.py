# Generated by Django 3.1.5 on 2021-02-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
    ]
