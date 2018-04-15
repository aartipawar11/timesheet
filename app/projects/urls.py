from django.conf.urls import url
from app.projects import views
app_name='projects'


urlpatterns = [
	url(r'',views.ProjectView.as_view()),
	# url(r'^assignproject$',views.AssignProject.as_view()),
	# url(r'',views.UserProjectView.as_view())
	url(r'^(?P<id>[0-9]+)$',views.ProjectView.as_view()),
]

