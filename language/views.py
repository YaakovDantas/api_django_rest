# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer