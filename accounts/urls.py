from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = "accounts"
urlpatterns = [
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password_reset/',views.password_reset, name='password_reset'),
    #path('passwordChanged/',views.pass_changed_success,name='changed' ),
    #path('login/', views.manage, name='changed'),
    path('login/', views.manage, name= 'login'),
    path('', views.home, name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='confirm_password_reset'),
    path('', views.home, name= 'home' ),
    path('logout/',views.logout_request, name='logout'),
    path('check_username/',views.check_username),
    #path('confirmAccount/<uidb64>/<token>/',views.confirmAccount, name= 'activate')
    path('confirmAccount/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('student/<uuid:id>/', views.manage, name='student'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_sent.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    path('', include('user_profile.urls', namespace='user_profile')),
    #path('', include('course.urls', namespace='course')),
    url('', include('course.urls', namespace='course')),
    #path('mentee/', views.signin, name= 'login'),
    # path('',include('hospital.urls')),
    # path('',include('doctor.urls')),
    # path('',include('patient.urls')),
]
#http://127.0.0.1:8000/reset/ZjExODQ3NjktYzEzNy00YTE1LWJjNTAtMmU3ZWRiNTM5ZmY5/5nt-f87a41a2d46c2ceb4aba/