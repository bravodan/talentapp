from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import reverse_lazy
from .forms import EmailValidationOnForgotPassword

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='usuario.login'),
    path('logout', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='usuario.logout'),
    path('reset/password_reset', auth_views.PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPassword,
        template_name='usuario/password_reset.html',),
        name='password_reset'
    ), 
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='usuario/password_reset_done.html'),
        name = 'password_reset_done'
    ),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('usuario.login'),
            template_name="usuario/password_reset_confirm.html"
        ),
        name='password_reset_confirm'),
]
