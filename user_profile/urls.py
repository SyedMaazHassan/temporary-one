from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "user_profile"
urlpatterns = [
    path('user_profile/<uuid:id>/', views.user_profile_view, name='profile'),
    path('instructor/<id>/', views.instructor_details_view, name='instructor_details'),
    path('instructors/', views.instructors_all_view, name='all_instructors'),
    path('editStudent/<uuid:id>/',views.editStudent),
    path('passwordChange/<uuid:id>/',views.passwordChange),
    #path('getwatingappointments/<uuid:id>/',views.getwatingappointments),
    path('addInstructor/', views.add_instructor),
    path('list/<uuid:id>/',views.get_list),
    #url(r'^course/', include(('course.urls', app_name='course'), namespace='course_single_')),
    #path('', include('course.urls', namespace='course')),
    
    #path('', include('course.urls', namespace='courses_namespace')),
    
]