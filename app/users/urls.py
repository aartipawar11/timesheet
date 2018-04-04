from django.conf.urls import url
from . import views
app_name='users'


urlpatterns = [
	url(r'^login$',views.Login.as_view(),name='login'),
	# url(r'^dashboard$',views.Login.as_view()),
	url(r'^login/(?P<user_id>[0-9]+)$',views.Login.as_view()),
	url(r'^(?P<user_id>[0-9]+)$',views.UserProfileList.as_view()), 
	url(r'',views.UserProfileList.as_view()), 
	# url(r'^(?P<user_id>[0-9]+)$',views.UpdateUserProfile.as_view()),
]