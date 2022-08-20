from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
	path('', views.PostList.as_view(), name='all'),
	path('create/', views.CreatePost.as_view(), name='create'),
	path('<username>/', views.UserPosts.as_view(), name='for_user'),
	#path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single'),
	path('delete/<pk>', views.DeletePost.as_view(), name='delete'),
	path('edit/<pk>', views.UpdatePost.as_view(), name='update'),
]