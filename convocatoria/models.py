from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import ContentTypeRestrictedFileField
#from usuarios.models import Aspirante
#from usuarios.models import Empresarial

# Create your models here.
class Convocatoria(models.Model):
    status_choices = [
        ('1', 'Abierta'),
        ('2', 'Cerrada'),
        ('3', 'Terminada')
    ]
    job_title = models.CharField(_('Cargo'), max_length=60)
    description = models.TextField(_('Descripción'))
    closing_date_time = models.DateTimeField(_('Fecha y hora de cierre'))
    status = models.CharField(_('Estado'), max_length=2, choices=status_choices, default='1')
    #company = models.ForeignKey(Empresarial, on_delete=models.CASCADE, verbose_name="Empresa")
    created_at = models.DateTimeField(_('fecha y hora de registro'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)

    class Meta:
        verbose_name = _('Convocatoria')
        verbose_name_plural = _('Convocatorias')

    def __str__(self):
        return self.job_title

class Postulacion(models.Model):
    #aspirate = models.ForeignKey(Aspirante, on_delete=models.CASCADE, verbose_name='aspirante')
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE, verbose_name='convocatoria')
    apply_date = models.DateTimeField(_('Fecha de postulación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)
    #unique_together = ('aspirante', 'convocatoria', 'apply_date')

class PostulacionAnonima(models.Model):
    full_name = models.CharField(_('Nombre completo'), max_length=80)
    curriculum = ContentTypeRestrictedFileField(_('Curriculo'), upload_to='curriculums/', content_types=['application/pdf',],max_upload_size=10485760)