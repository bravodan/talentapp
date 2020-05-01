from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Convocatoria, PostulacionAnonima
from .validators import file_size
from django.core.validators import FileExtensionValidator

#Formulario para que una empresa cree una convocatoria
class JobOfferForm(forms.ModelForm):
    job_title = forms.CharField(label=_('Cargo'), max_length=60)
    description = forms.CharField(label=_('Descripción'))
    closing_date_time = forms.DateTimeField(label=_('Fecha y hora de cierre'))
    class Meta:
        model = Convocatoria
        exclude = ('company','candidate_applications','anonymous_applications')

    def save(self, commit=True):
        return super().save(commit=commit)

#Formulario para que un usuario anonimo aplique a una convocatoria
class AnonymousApplyJobOfferForm(forms.ModelForm):
    full_name = forms.CharField(label=_('Nombre completo'), min_length=5, max_length=120)
    curriculum = forms.FileField(label=_('Curriculo'), validators=[file_size, FileExtensionValidator(['pdf'])])

    class Meta:
        model = PostulacionAnonima
        exclude = ('convocatoria',)

    def save(self, commit=True):
        return super().save(commit=commit)