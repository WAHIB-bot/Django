# Generated by Django 5.1 on 2024-10-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='title',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='banner',
            name='bgcolor',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='btnlink',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='btntext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='subheading',
            field=models.TextField(blank=True, null=True),
        ),
    ]
