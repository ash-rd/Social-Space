# Generated by Django 4.0.1 on 2022-08-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_facebook_profile_instagram_profile_twitter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
