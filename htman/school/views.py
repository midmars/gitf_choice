# <!--   -*- coding: UTF-8 -*-  --> 
from django.shortcuts import render,render_to_response
from django.http import HttpResponse 
from models import *
from django.shortcuts import redirect
import random
from django.core.exceptions import ObjectDoesNotExist
import json
from school.function import *

def index(request):
	request.session['status']=1 #1是學生2是老師
	list_student = Member.objects.filter(weight=1)
	list_professor = Member.objects.filter(weight=2)
	
	return render(request, 'index.html',locals())



	



def lottery(request):
	imgr = Member.objects.all()
	list_student = Member.objects.filter(weight=1)
	list_professor = Member.objects.filter(weight=2)
	return render(request,"gift.html",locals())


def id_s(request):
	data = {}

	status = 1

	try:
		status = request.GET.get('status')


	except:
		pass

	request.session['status'] = status

	return HttpResponse(json.dumps(data))

def new_member(request):
	try:
		name = request.GET.get('member_name')

		if name:

			result = member.member_double(name)

			#沒重複
			if result == 0:

				weight = request.session['status']

				if weight == 2:
					status = "professor"
				else:
					status = "student"

				member_img = name+".jpg"


				save_it = Member(name=name,weight=weight,status=status,member_img=member_img)
				save_it.save()



	except:
		ss = "名稱重複"

	list_student = Member.objects.filter(weight=1)
	list_professor = Member.objects.filter(weight=2)
	





	return  render_to_response("list.html",locals())


def delete_member(request):
	try:
		name = request.GET.get('name')

		Member.objects.filter(name=name).delete()
		ss = "刪除成功"

	except:
		pass

	list_student = Member.objects.filter(weight=1)
	list_professor = Member.objects.filter(weight=2)
	





	return  render_to_response("list.html",locals())


def giver(request):
	
	member_all = Member.objects.all()
	
	x = []
	for y in member_all:
		if y.weight == 2 :
			x.append(y.name)
			x.append(y.name)
		else:
			x.append(y.name)
	
		
	giver = x[random.randint(0,len(x)-1)]

	member = Member.objects.get(name=giver)





	
	
	return render(request, 'giver.html',locals())

















	
	
