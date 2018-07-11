from django.conf.urls import url, include
#from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.LanguageView)

urlpatterns = [
    url('',include(router.urls))

]