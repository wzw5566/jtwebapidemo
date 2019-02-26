# -*- coding:UTF-8 -*-
from django.db import models

#导入django自带的User模型进行扩展
from django.contrib.auth.models import AbstractUser

class Role(models.Model):

    """
    用户角色
    """
    role_name = models.CharField(max_length=100, verbose_name="角色名", unique=True, help_text="角色名")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name
        #使用自定义指定的表名jt_role
        db_table = "jt_role"

    def __str__(self):
        return self.role_name


class Department(models.Model):

    """
    部门
    """
    depat_name = models.CharField(max_length=64, verbose_name="部门名称", unique=True, help_text="部门名称")
    depat_fid = models.IntegerField(verbose_name="父级部门id", default=0, help_text="父级部门id")

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name
        db_table = "jt_department"

    def __str__(self):
        return self.depat_name



class UserProfile(AbstractUser):
    """
    在Django的User模型上进行拓展，自带id,is_active用户状态字段
    """
    name = models.CharField(max_length=64, verbose_name="姓名")
    avatar = models.URLField(verbose_name="用户头像链接地址", null=True, blank=True, default='', help_text="头像地址")
    #使用不定义外键形式实现，定义用户与部门的id,在逻辑层实现约束
    depat_id = models.IntegerField(verbose_name="部门id",help_text="部门id")


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = "jt_user"

class UserRole(models.Model):
    """
    用户角色关系，为提高性能，不使用manytomany来实现
    """
    user_id = models.IntegerField(verbose_name="用户id", help_text="用户表id")
    role_id = models.IntegerField(verbose_name="角色id", help_text="角色表id")

    class Meta:
        verbose_name = "用户角色关系"
        verbose_name_plural = verbose_name
        db_table = "jt_user_role"
