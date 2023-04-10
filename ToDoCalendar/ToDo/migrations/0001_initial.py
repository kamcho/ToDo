# Generated by Django 4.0.2 on 2023-04-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('about', models.TextField(max_length=500)),
                ('date', models.DateTimeField()),
                ('reminder', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
