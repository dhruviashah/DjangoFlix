# Generated by Django 3.2 on 2021-04-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video_id', models.CharField(max_length=250)),
            ],
        ),
    ]
