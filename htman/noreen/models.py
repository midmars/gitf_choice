# <!--   -*- coding: UTF-8 -*-  -->
from django.db import models



class Member(models.Model):
    member_pk = models.AutoField(max_length=255,primary_key=True)
    member_name = models.CharField(max_length=255,default="")

    #排名
    member_rank = models.IntegerField(default=0)

   
    #測驗時間
    test_date = models.DateTimeField(blank=True, null=True)

    #是否完成測驗
    finish = models.IntegerField(default=0)

    #總分
    value_sum = models.IntegerField(default=0)
    #邊緣性人格
    result_edge = models.CharField(max_length=255,default="")
    #憂鬱症
    result_depression = models.CharField(max_length=255,default="")
    #焦慮症
    result_anxiety = models.CharField(max_length=255,default="")




class Question(models.Model):
	question_pk = models.AutoField(max_length=255,primary_key=True)
	number = models.IntegerField()
	article = models.CharField(max_length=255)
	attribute = models.IntegerField()


class QAE(models.Model):
	explain_pk = models.AutoField(max_length=255,primary_key=True)
	name = models.CharField(max_length=255,default="")

class IMG(models.Model):
	IMG_pk = models.AutoField(max_length=255,primary_key=True)
	pwd = models.CharField(max_length=255)
	title = models.CharField(max_length=255,default="")
	article = models.TextField()

class MQV(models.Model):
	MQV_pk = models.AutoField(max_length=255,primary_key=True)
	qn = models.IntegerField()
	member_pk = models.IntegerField()
	value = models.IntegerField(default=-1)





