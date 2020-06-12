from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='myApp-home'),
	path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('home/', views.home, name='myApp-home'),
	path('about/', views.about, name='myApp-about'),

]