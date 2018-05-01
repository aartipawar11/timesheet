from django.conf.urls import url
from app.tasks import views
app_name='tasks'

urlpatterns = [
	
	# url(r'^(?P<id>[0-9]+)$',views.TaskView.as_view()),

	url(r'^edittask$',views.EditTask.as_view()),
	url(r'^edittask/(?P<user_id>[0-9]+)$',views.EditTask.as_view()),
	url(r'^taskdetail/(?P<user_id>[0-9]+)$',views.UserTaskDatewise.as_view()),
	url(r'',views.TaskView.as_view()),
]
