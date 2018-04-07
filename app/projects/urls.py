from django.conf.urls import url
from app.projects import views

app_name='projects'

urlpatterns = [
	url(r'',views.ProjectView.as_view()),
	]