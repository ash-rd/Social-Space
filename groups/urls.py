from django.urls import path
from . import views

app_name = "group"

urlpatterns = [
	path('', views.ListGroup.as_view(), name='g_list'),
	
	# users cannont create new groups
	#path('new/', views.CreateGroup.as_view(), name='create'),
	
	path('<slug>/', views.SingleGroup.as_view(), name='detail'),
	
	#path('new/', views.CreateGroup.as_view(), name='create'),
]