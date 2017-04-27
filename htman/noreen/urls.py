from django.conf.urls import patterns, url,include
 
from noreen import views
 
urlpatterns = patterns('noreen.views',
    # ex: /polls/   
   
    
    
  	url(r'^$','login',name='login'),

    url(r'^home/$','home',name='home'),

    url(r'^check/$','check',name='check'),
    url(r'^out/$','out',name='out'),
    

    url(r'^login_member/$','login_member',name='login_member'),
	


    
   
)