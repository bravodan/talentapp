from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from .forms import JobOfferForm
from .models import Convocatoria, Postulacion, PostulacionAnonima
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateJobOfferView(FormView):
    form_class = JobOfferForm
    template_name = 'convocatoria/create_job_offer.html'
    success_url = 'misConvocatorias'

    def form_valid(self, form):
        form.instance.company = self.request.user
        form.save()
        return super().form_valid(form)
        
@method_decorator(login_required, name='dispatch')
class AllJobOffersListView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/all_job_offers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_applicants = 0
        if(Postulacion.objects.all().count() > 0):
            ofertas = Convocatoria.objects.get(company=self.request.user)
            count_applicants = Postulacion.objects.filter(convocatoria=ofertas).count()
        context['all_job_offers'] = Convocatoria.objects.filter(company=self.request.user)
        context['applicants_number'] = count_applicants
        context['today'] = date.today()
        return context

@method_decorator(login_required, name='dispatch')
class JobOfferDetailView(DetailView):
    model = Convocatoria
    template_name = 'convocatoria/job_offer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicants_users'] = Postulacion.objects.filter(convocatoria=self.kwargs['pk'])
        context['anonymous_applicants'] = PostulacionAnonima.objects.filter(convocatoria=self.kwargs['pk'])
        return context