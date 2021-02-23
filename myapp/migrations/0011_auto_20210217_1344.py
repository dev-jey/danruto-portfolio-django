# Generated by Django 3.1.2 on 2021-02-17 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_project_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_type', to='myapp.projecttypes'),
        ),
    ]