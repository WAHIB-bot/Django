# Generated by Django 5.1 on 2024-09-12 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('decsription', models.CharField(max_length=500)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollemnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='app1.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='app1.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
