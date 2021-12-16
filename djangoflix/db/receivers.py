from django.utils import timezone
from django.utils.text import slugify

from .models import PublishStateOptions
# Create your models here.

def publish_state_pre_save(sender, instance, *args, **kwargs):
	if instance.state == PublishStateOptions.PUBLISH and instance.publish_timestamp is None:
		print("save as timestamp for published")
		instance.publish_timestamp = timezone.now()
	else:
		instance.publish_timestamp = None

def slugify_pre_save(sender,instance,*args,**kwargs):
	title = instance.title
	slug = instance.slug
	if slug is None:
		instance.slug = slugify(title)
