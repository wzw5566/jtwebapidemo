# -*- coding:UTF-8 -*-

from django.urls import path, include, re_path

from rest_framework.routers import reverse
#
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register(r'roles', views.RoleModeViewSet, base_name='roles')
router.register(r'users', views.UserModelViewSet, base_name='users')
router.register(r'depat', views.DepatModelViewSet, base_name='depat')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

]