# -*- coding: UTF-8 -*-

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import mixins
from users.serializers import RoleSerializer, DepartmentSerializer, UserRoleSerializer, UserSerializer,UserInfoSerializer
from users.models import Role, Department, UserRole


from rest_framework.mixins import CreateModelMixin

User = get_user_model()


class RoleModeViewSet(viewsets.ModelViewSet):

    """
    查看和编辑角色实例的视图集。
    """
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class DepatModelViewSet(viewsets.ModelViewSet):

    """
    查看和编辑部门的实例的视图集
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class UserModelViewSet(viewsets.ModelViewSet):
    """
    查看和编辑用户的实例的视图集
    """
    # serializer_class = UserSerializer
    serializer_class = UserSerializer
    queryset = User.objects.all()

