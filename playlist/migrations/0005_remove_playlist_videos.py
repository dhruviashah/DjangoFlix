# Generated by Django 3.2 on 2021-06-06 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_alter_playlist_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='videos',
        ),
    ]
