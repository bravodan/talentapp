from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('email',)


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Usuario.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("No existe un usuario registrado con este email")
            self.add_error('email', msg)
        return email