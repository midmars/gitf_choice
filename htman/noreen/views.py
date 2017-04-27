# <!--   -*- coding: UTF-8 -*-  --> 

from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse 
from django.shortcuts import redirect
from datetime import timedelta,datetime
from django.utils import timezone
import json
from noreen.models import *
# from article.function import *



from noreen.models import *

from noreen.function import *


#! /usr/bin/env python




def login(request):

	member = Member.objects.filter(finish=1).order_by('member_rank')

	return render(request, "login.html", locals())


def out(request):

	
	try:

		qn = request.session['qn']
		mp  = request.session['mp']

		MQV.objects.filter(member_pk=mp).delete()
		Member.objects.filter(member_pk=mp).delete()

		del request.session['mp']
		del request.session['qn']

		Return.rank()
		

	except:
		pass

	return redirect("/noreen/")


		
	
	


def login_member(request):

	data = {}
	errors = []


	member_name = request.GET.get('member_name')


	#檢驗
	if not member_name:
		errors.append("請輸入姓名")
	else:
		if Return.member_exist(member_name) == 0:
			errors.append("名稱被用過了喔")
	

	
	


	if not errors:

		member_pk = Member_f.member_login(member_name)
		request.session['mp'] = member_pk
		request.session['qn'] = 1

		data['state'] = 1
	else:
		data['errors'] = errors
		data['state'] = 0


	return HttpResponse(json.dumps(data))



def home(request):

	qn = request.session['qn']
	mp  = request.session['mp']
	img = IMG.objects.all().order_by('?')[:3]
	
	question = Question.objects.get(number=qn)

	kk = len(MQV.objects.filter(member_pk=mp,value=-1))
	request.session['kk'] = kk
		

	
	
	return render(request, "motherboard.html", locals())


def check(request):

	data = {}
	
	

	answer = request.GET.get('answer')

	answer = int(answer)
	qn = request.session['qn']
	mp  = request.session['mp']

	qn = Member_f.member_answer(mp,qn,answer)

	state = 0

	kk = len(MQV.objects.filter(member_pk=mp,value=-1))
	request.session['kk'] = kk
		

	if qn == 31:
		#答題完成
		state = 1
	else:
		request.session['qn'] = qn
		
		

	

	if state == 1:
		# del request.session['mp']
		# del request.session['qn']
		pass


	data['state'] = state





	return HttpResponse(json.dumps(data))
