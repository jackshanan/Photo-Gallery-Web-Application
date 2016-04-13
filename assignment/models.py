from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class Album(models.Model):
	image_url = models.CharField(max_length=200)
	user = models.ForeignKey(User,)
	time_added = models.DateTimeField(default=timezone.now)
	retweet_count = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.username