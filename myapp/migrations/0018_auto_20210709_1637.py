# Generated by Django 3.1.6 on 2021-07-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20210304_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
    ]
