from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from djangoflix.db.models import PublishStateOptions
from .models import Video
# Create your tests here.

class VideoModelTestCase(TestCase):
	def setUp(self):
		self.obj_a = Video.objects.create(title="My title", video_id='V1')
		self.obj_b = Video.objects.create(title="My title", video_id='V2', state=PublishStateOptions.PUBLISH)

	def test_slug_field(self):
		title = self.obj_a.title
		test_slug = slugify(title)
		self.assertEqual(test_slug,self.obj_a.slug)

	def test_valid_title(self):
		title="My title"
		qs = Video.objects.filter(title=title)
		message = "Test value is not True"
		self.assertTrue(qs.exists(),message)

	def test_created_count(self):
		qs = Video.objects.all()
		message = "Test values are not same" 
		self.assertEqual(qs.count(),2,message)

	def test_draft_case(self):
		qs = Video.objects.filter(state = PublishStateOptions.DRAFT)
		self.assertEqual(qs.count(),1)

	def test_publish_case(self):
		now = timezone.now()
		qs = Video.objects.filter(state = PublishStateOptions.PUBLISH, publish_timestamp__lte = now)
		self.assertEqual(qs.count(),1)

	def test_publish_manager(self):
		published_query = Video.objects.all().published()
		published_query2 = Video.objects.published()
		self.assertEqual(published_query.count(),published_query2.count())