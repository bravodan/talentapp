from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.models import Usuario

# Create your models here.

class PostulacionAnonima(models.Model):
    full_name = models.CharField(_('Nombre completo'), max_length=120)
    curriculum = models.FileField(_('Curriculo'), upload_to='curriculums/')
    apply_date = models.DateTimeField(_('Fecha de postulación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)

    class Meta:
        verbose_name = _('Postulacion Anónima')
        verbose_name_plural = _('Postulaciones Anónimas')

class Convocatoria(models.Model):
    status_choices = [
        ('1', _('Abierta')),
        ('2', _('Cerrada')),
        ('3', _('Terminada'))
    ]
    job_title = models.CharField(_('Cargo'), max_length=60)
    description = models.TextField(_('Descripción'))
    closing_date_time = models.DateTimeField(_('Fecha y hora de cierre'))
    status = models.CharField(_('Estado'), max_length=2, choices=status_choices, default='1')
    company = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Empresa")
    anonymous_applications = models.ManyToManyField(PostulacionAnonima)
    created_at = models.DateTimeField(_('fecha y hora de registro'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)

    class Meta:
        verbose_name = _('Convocatoria')
        verbose_name_plural = _('Convocatorias')

    def __str__(self):
        return self.job_title
        
class Postulacion(models.Model):
    candidate = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='aspirante')
    apply_date = models.DateTimeField(_('Fecha de postulación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)
    unique_together = ('aspirante', 'convocatoria', 'apply_date')
    announcement = models.ForeignKey(Convocatoria, on_delete=models.CASCADE, verbose_name='aspirante')

    class Meta:
        verbose_name = _('Postulacion')
        verbose_name_plural = _('Postulaciones')

