# Generated by Django 4.1.7 on 2023-03-26 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='project_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
    ]
