from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "course"


urlpatterns = [
    #path('event/<id>', views.course_details, name= 'event'),
    path('upcoming_events/', views.upcoming_events_view, name= 'upcoming_events'),
    path('', include('user_profile.urls', namespace='user_profile_namespace')),
    #path('course/<slug>/', views.course_single, name= 'course_single')
]