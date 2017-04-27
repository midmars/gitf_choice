from django.db import models

# Create your models here.
class Member(models.Model):
	member_pk = models.AutoField(max_length=255,primary_key=True)
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=255)
	weight = models.IntegerField()
	member_img= models.CharField(max_length=255,null=True)