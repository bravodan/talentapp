from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from convocatoria.validators import ContentTypeRestrictedFileField

# Create your models here.
class Usuario(AbstractUser):
    username = models.CharField(_('Nombre de usuario'), max_length=30, default="default username")
    email = models.EmailField(_('direccion de correo electronico'), unique=True)
    first_name = models.CharField(_('Nombres'), max_length=40)
    last_name = models.CharField(_('Apellidos'), max_length=40)
    is_applicant_user = models.BooleanField(_('Es usuario aspirante'), default=False)
    is_business_user = models.BooleanField(_('Es usuario empresarial'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')

    def __str__(self):
        return self.username