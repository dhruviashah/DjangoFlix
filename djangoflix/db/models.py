from django.db import models
# Create your models here.

class PublishStateOptions(models.TextChoices):
		PUBLISH = 'PU','publish'
		DRAFT = 'DR','draft'
