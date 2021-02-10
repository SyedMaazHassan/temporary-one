from django.urls import path
from . import views

urlpatterns = [
    path('student/<uuid:id>/', views.student_view, name='student'),
    path('editStudent/<uuid:id>/',views.editStudent),
    path('passwordChange/<uuid:id>/',views.passwordChange),
    #path('getwatingappointments/<uuid:id>/',views.getwatingappointments),
    path('list/<uuid:id>/',views.get_list),
]