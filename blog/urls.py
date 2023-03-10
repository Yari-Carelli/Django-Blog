"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import (
    index, blog, post, search,
    post_create, post_update, post_delete)
# from posts.views import (
#     index,
#     search,
#     post_list,
#     post_detail,
#     post_create,
#     post_update,
#     post_delete,
#     IndexView,
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls'))
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', IndexView.as_view(), name='home'),
#     path('blog/', PostListView.as_view(), name='post-list'),
#     path('search/', search, name='search'),
#     path('create/', PostCreateView.as_view(), name='post-create'),
#     path('post/<id>/', PostDetailView.as_view(), name='post-detail'),
#     path('post/<id>/update/', PostUpdateView.as_view(), name='post-update'),
#     path('post/<id>/delete/', PostDeleteView.as_view(), name='post-delete'),
#     path('tinymce/', include('tinymce.urls')),
#     path('accounts/', include('allauth.urls'))
# ]