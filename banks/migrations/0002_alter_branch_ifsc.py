# Generated by Django 5.1.7 on 2025-06-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='ifsc',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
