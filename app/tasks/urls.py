
from django.conf.urls import url
from app.tasks import views
app_name='tasks'


urlpatterns = [
	url(r'',views.TaskView.as_view()),
	
]