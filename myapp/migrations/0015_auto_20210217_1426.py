# Generated by Django 3.1.2 on 2021-02-17 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210217_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='linkedin',
            new_name='instagram',
        ),
    ]
