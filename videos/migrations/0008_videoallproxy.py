# Generated by Django 3.2 on 2021-05-03 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_video_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAllProxy',
            fields=[
            ],
            options={
                'verbose_name': 'All Video',
                'verbose_name_plural': 'All Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]