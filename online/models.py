from django.db import models


# -*- coding: UTF-8 -*-

# Create your models here.

class user(models.Model):
    GENDER_CHOICES = ((1,'Male'),(2,'Female'))
    st_username = models.CharField(max_length=50, primary_key=True)
    st_name = models.CharField(max_length=50, null=False)
    st_sex = models.IntegerField(choices=GENDER_CHOICES,null=False)
    st_age = models.CharField(max_length=50, null=False)
    st_password = models.CharField(max_length=50, null=False)
    st_address = models.CharField(max_length=250, null=False)


class buy_device(models.Model):
    buy_no = models.AutoField(primary_key=True)
    de_no = models.CharField(max_length=50, null=False)
    de_btime = models.DateTimeField(auto_now_add=False, null=False)
    de_ptime = models.DateTimeField(auto_now_add=False, null=False)
    buy_num = models.IntegerField(null=False)
    beizhu = models.CharField(max_length=250, null=True)


class lend_device(models.Model):
    lend_no = models.AutoField(primary_key=True)
    de_no = models.CharField(max_length=50, null=False)
    st_no = models.CharField(max_length=50, null=False)
    lend_date = models.DateTimeField(auto_now_add=False, null=False)
    lend_num = models.IntegerField(null=False)
    beizhu = models.CharField(max_length=250, null=True)


class repair_device(models.Model):
    repair_no = models.AutoField(primary_key=True)
    st_no = models.CharField(max_length=50, null=False)
    de_no = models.CharField(max_length=50, null=False)
    destroy_date = models.DateTimeField(auto_now_add=False, null=False)
    repair_num = models.IntegerField(null=False)
    beizhu = models.CharField(max_length=250, null=True)


class device(models.Model):
    de_no = models.CharField(max_length=50, primary_key=True)
    de_name = models.CharField(max_length=50, null=False)
    de_allnum = models.IntegerField(null=False)
    de_repnum = models.IntegerField(null=False)
    de_lennum = models.IntegerField(null=False)
    de_lasnum = models.IntegerField(null=False)

