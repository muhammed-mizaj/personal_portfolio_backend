# Generated by Django 4.2.1 on 2023-05-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_project_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
