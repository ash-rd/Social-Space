# Generated by Django 4.0.1 on 2022-08-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank='True', default='', max_length=100),
        ),
    ]