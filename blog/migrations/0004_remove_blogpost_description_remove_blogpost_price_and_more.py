# Generated by Django 5.1.6 on 2025-03-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_author_blogpost_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='price',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
