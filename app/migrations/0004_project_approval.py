# Generated by Django 4.1.7 on 2023-03-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_sample_project_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
