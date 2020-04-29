from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Convocatoria

class JobOfferForm(forms.ModelForm):
    job_title = forms.CharField(label=_('Cargo'), max_length=60)
    description = forms.CharField(label=_('Descripción'))
    closing_date_time = forms.DateTimeField(label=_('Fecha y hora de cierre'))
    class Meta:
        model = Convocatoria
        exclude = ('company',)

    def save(self, commit=True):
        return super().save(commit=commit)