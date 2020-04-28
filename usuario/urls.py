from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='usuario.login'),
    path('logout', auth_views.logout_then_login, name='usuario.logout'),
]
