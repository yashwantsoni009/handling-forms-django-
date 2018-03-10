from __future__ import unicode_literals
from django.db import models

# Create your models here.
class profile(models.Model):
	name=models.CharField(max_length=120)
	description=models.TextField(default='zibber jabber')
	location=models.CharField(max_length=120,default='rani bazar')
	def __unicode__(self):
		return self.name