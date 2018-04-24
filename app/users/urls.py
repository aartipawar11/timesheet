from django.conf.urls import url
from . import views
# from django.contrib.auth import views as auth_views
app_name='users'


urlpatterns = [
	url(r'^login$',views.Login.as_view(),name='login'),
	url(r'^dashboard$',views.Dashboard.as_view()),
	url(r'^userprofile$',views.UserDetail.as_view()),
	url(r'^admindashboard$',views.AdminDashboard.as_view()),
	url(r'^admindetails$',views.AdminDetails.as_view()),
	url(r'^adduser$',views.AddUser.as_view()),
	url(r'^assignproject$',views.AssignProject.as_view()),
	url(r'^assignprojectdetails$',views.AssignProjectApi.as_view()),
	url(r'^workdetails$',views.WorkDetails.as_view()),
	url(r'^addproject$',views.AddProject.as_view()),

	url(r'^viewprojects$',views.ViewProject.as_view()),

	url(r'^login/(?P<user_id>[0-9]+)$',views.Login.as_view()),
	url(r'^(?P<user_id>[0-9]+)$',views.UserProfileList.as_view()),
	url(r'^taskdetail$',views.UserTaskDetails.as_view()),
	url(r'^taskdetail/(?P<user_id>[0-9]+)$',views.UserTaskDatewise.as_view()),
	# url(r'^datewise$',views.DateWiseWork.as_view()),
	url(r'^deleteuser$',views.DeleteUser.as_view()),
	# url(r'^edittask$',views.EditTask.as_view()),
	# url(r'^edittask/(?P<user_id>[0-9]+)$',views.EditTask.as_view()),
	# url(r'^(?P<user_id>[0-9]+)$',views.UpdateUserProfile.as_view()),
	url(r'',views.UserProfileList.as_view()),
]