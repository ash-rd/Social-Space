# Generated by Django 4.0.1 on 2022-04-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', unique=True),
        ),
    ]
