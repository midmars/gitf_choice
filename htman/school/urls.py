from django.conf.urls import patterns, url,include
 
from school import views
 
urlpatterns = patterns('school.views',
    # ex: /polls/   
   
    
    
  	url(r'^$','index'),
    url(r'^login/$','login'),
	url(r'^result/$','lottery'),
	url(r'^id_s/$','id_s'),
	url(r'^new_member/$','new_member'),
	url(r'^delete_member/$','delete_member'),
	url(r'^gift/$','gift'),
	url(r'^giver/$','giver'),





    
   
)