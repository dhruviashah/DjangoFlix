# Generated by Django 3.2 on 2021-05-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_rename_title_video_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
    ]
