# <!--   -*- coding: UTF-8 -*-  --> 
from noreen.models import *
from datetime import timedelta,datetime

import hashlib
import random


#回報錯誤
class Return(object):


	@classmethod
	def member_exist(self,member_name):

		result = 1

		m = Member.objects.filter(member_name=member_name,finish=1)

		if len(m) > 0:

			result = 0

		return result

	@classmethod
	def rank(self):




		member = Member.objects.filter(finish=1).order_by('-value_sum','-test_date')

		rank = 1
		for x in member:
			Member.objects.filter(member_pk=x.member_pk).update(member_rank=rank)
			rank = rank+1

		return None












class Member_f(object):

	
	@classmethod
	def member_login(self,member_name):

		member = Member(

			member_name = member_name,
			)

		member.save()

		member_pk = Member.objects.get(member_name=member_name).member_pk

		for x in range(1,31,1):

			save_it = MQV(
				qn=x,
				member_pk=member_pk,

				)
			save_it.save()

		return member_pk


	@classmethod
	def member_answer(self,member_pk,question_number,answer):

		#0 = 未完成
		#1 = 答題結束
		qn = question_number
		
		MQV.objects.filter(member_pk=member_pk,qn=question_number).update(value=answer)

		mqv_check = MQV.objects.filter(member_pk=member_pk,value=-1)

		if len(mqv_check) == 0:
			Member_f.member_finish(member_pk)
			qn=31
		else :

			x = random.randrange(0,len(mqv_check),1)
			qn = mqv_check[x].qn

			# qn = 2


			
			
			
		

		return qn




	@classmethod
	def member_finish(self,member_pk):

		
		mqv = MQV.objects.filter(member_pk=member_pk).order_by('qn')

		value_sum = 0 
		value_edge = 0
		value_depression = 0
		value_anxiety = 0

		for x in mqv:
			value_sum = value_sum+x.value

			#焦慮症 anxiety
			if x.qn>20:
				value_anxiety = value_anxiety+x.value

			#邊緣性人格 edge
			elif x.qn>10:
				value_edge = value_edge+x.value

			#憂鬱症 depression
			else:
				value_depression = value_depression+x.value 





		

		result_depression = ""
		if value_depression>=16:
			result_depression = "嚴重*"
		elif value_depression>=10:
			result_depression = "中度*"
		else:
			result_depression ="心理健康"

		result_anxiety = ""
		if value_anxiety>=16:
			result_anxiety = "嚴重*"
		elif value_anxiety>=10:
			result_anxiety = "中度*"
		else:
			result_anxiety ="心理健康"


		result_edge = ""
		if value_edge >15:
			result_edge ="第五級*"
		elif value_edge >12:
			result_edge ="第四級*"
		elif value_edge >9:
			result_edge ="第三級*"
		elif value_edge >6:
			result_edge ="第二級"
		elif value_edge >3:
			result_edge ="第一級"
		else:
			result_edge ="完全健康"





		
		Member.objects.filter(member_pk=member_pk).update(
			value_sum = value_sum,
			test_date = datetime.now(),			
			finish =1,
			result_depression = result_depression,
			result_anxiety = result_anxiety,
			result_edge = result_edge,
			)

		Return.rank()
		

		# member = Member.objects.filter(finish=1).order_by('-value_sum','-test_date')

		# rank = 1
		# for x in member:
		# 	Member.objects.filter(member_pk=x.member_pk).update(member_rank=rank)
		# 	rank = rank+1


		MQV.objects.filter(member_pk=member_pk).delete()
		

	

		return None



		