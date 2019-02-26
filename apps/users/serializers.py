# -*- coding: UTF-8 -*-
from django.contrib.auth import get_user_model
from users.models import Role, Department, UserRole
from rest_framework import serializers

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    """
    角色序列化
    """

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    注册用户序列化
    """

    roles = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ("username", "name", "password",  "avatar", "depat_id", "roles")


    def get_roles(self, obj):
        """
        自定义角色的序列化显示
        """
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        role_list = []
        for item in roles:
            role_list.append(item.role_name)
        return role_list



    def create(self, validated_data):


        user = User.objects.create(** validated_data)

        try:

            #重点：从原始的请求数据中拿到不在model序列化中的roles数据
            role_list = self.initial_data["roles"]

            #对获得role列表数据进行循环添加
            for item in role_list:
                #为第三张关系表添加数据，user_id ,role_id
                UserRole.objects.create(user_id=user.id, role_id=item)

        except Exception as e:

            print(e)

        return user




class UserInfoSerializer(serializers.Serializer):
    """
    用户登录后返回用户信息序列化
    SerializerMethodField自定义的字段，为read_only只读字段
    """
    name = serializers.CharField(max_length=64)

    avatar = serializers.URLField()

    roles = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ("name", "avatar", "roles")


    def get_roles(self, obj):
        """
        自定义角色的序列化显示
        """
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        role_list = []
        for item in roles:
            role_list.append(item.role_name)
        return role_list



class DepartmentSerializer(serializers.ModelSerializer):
    """
    部门序列化
    """

    class Meta:
        model = Department
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    """
    用户角色关系序列表
    """

    class Meta:
        model = UserRole
        fields = '__all__'
