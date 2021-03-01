from django.urls import path, include
from . import views


urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('blogs', views.BlogList.as_view(), name='blog_list'),
    path('blogs/<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
    path('comments', views.CommentList.as_view(), name='comment_list'),
]
