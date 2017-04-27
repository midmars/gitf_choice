# <!--   -*- coding: UTF-8 -*-  --> 

from school.models import *
import random
import json



class member(object):
	@classmethod
	def member_double(self,name):
		result = 0
		

		member = Member.objects.filter(name=name)

		if len(member) == 0 :
			pass

		else:
			result = 1
		

		return result
	



class Lottery(object):
	
	@classmethod
	def weight(self):
		choice_weight=0
		member_list=Member.objects.all()
		for i in member_list:
			choice_weight+=i.weight
		return choice_weight
	@classmethod
	def lottery_(self,weight,dict):
			results=[]
			random_choice = random.randint(0,weight-1)
			s = 0
			for w in dict.items():
				s += w[1]
				if s >random_choice:
						break;
		#results=json.dumps(results, encoding="UTF-8", ensure_ascii=False) ##解決字典中文轉化
			if w[0] not in results:
				results.append(w[0])
			#if w[0] in results:	
			return results[0]

	# @classmethod
	# def image(self,choice):
	# 	choice_image=''
	# 	choice_=Member.objects.filter(member_pk=choice)
	# 	for i in choice_:
	# 	 	chocie_image=i.member_img
	# 	return choice_image