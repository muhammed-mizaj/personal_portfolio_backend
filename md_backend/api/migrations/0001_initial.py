# Generated by Django 4.0.1 on 2022-01-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='code.jpg', null=True, upload_to='')),
                ('desciption', models.CharField(max_length=200)),
                ('sourcecodelink', models.CharField(blank=True, max_length=200, null=True)),
                ('view_link', models.CharField(blank=True, max_length=200, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
