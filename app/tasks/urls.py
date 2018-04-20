
from django.conf.urls import url
from app.tasks import views
app_name='tasks'


urlpatterns = [
	url(r'',views.TaskView.as_view()),
	url(r'^(?P<user_id>[0-9]+)$',views.TaskView.as_view()),
]