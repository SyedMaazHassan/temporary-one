from django.urls import path, include
from . import views
from accounts.views import logout

urlpatterns = [
    path('changePassword/<uuid:id>/', views.changePassword),
    path('saidatech_admin/<uuid:id>/', views.saidatech_admin_view),
    path('saidatech_admin/<uuid:id>/addInstructor', views.add_instructor),
    path('accounts/', include(('accounts.urls', 'home'), namespace='password_reset_confirm'))
]
