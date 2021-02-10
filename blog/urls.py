from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = "blog"
urlpatterns = [
    path('blog/', views.blog_view, name= 'blog'),
]