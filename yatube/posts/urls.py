from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    ##path('group/<slug:slug>', views.index),
    path('post/list', views.group_posts, name = 'posts'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('post/<int:pk>/',
        views.post_detail
    ),
]

