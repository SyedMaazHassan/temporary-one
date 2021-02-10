from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "course"


urlpatterns = [
    path('course/<id>', views.course_details, name= 'course_details'),
    path('courses/', views.course_list, name= 'courses'),
    path('', include('user_profile.urls', namespace='user_profile_namespace')),
    #path('course/<slug>/', views.course_single, name= 'course_single')
]