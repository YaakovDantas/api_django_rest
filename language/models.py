# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from rest_framework import 
# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length = 50)
	paradigm = models.CharField(max_length = 50)

	def __str__(self):
		return self.name