from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views import View
from .forms import JobOfferForm, AnonymousApplyJobOfferForm
from .models import Convocatoria, Postulacion, PostulacionAnonima
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import FileResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from usuario.decorators import business_required
from usuario.decorators import candidate_required

# Create your views here.
class AllJobOffersListView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/all_job_offers.html'
    ordering = ['closing_date_time']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context

class AnonymousApplyJobOfferView(FormView):
    form_class = AnonymousApplyJobOfferForm
    template_name = 'convocatoria/anonymous_apply_job_offer.html'
    success_url = '/'

    def form_valid(self, form):
        announcement = Convocatoria.objects.get(pk=self.kwargs.get('pk'))
        anonymous_apply = form.save()
        announcement.anonymous_applications.add(anonymous_apply)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['convocatoria'] = Convocatoria.objects.get(pk=self.kwargs.get('pk'))
        context['today'] = timezone.now()
        return context

@method_decorator(business_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class CreateJobOfferView(FormView):
    form_class = JobOfferForm
    template_name = 'convocatoria/create_job_offer.html'
    success_url = 'misConvocatorias'

    def form_valid(self, form):
        form.instance.company = self.request.user
        form.save()
        return super().form_valid(form)

@method_decorator(business_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AllCompanyJobOffersListView(ListView):
    model = Convocatoria
    template_name = 'convocatoria/all_company_job_offers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcements = Convocatoria.objects.filter(company=self.request.user)
        apply_count = []
        for announcement in announcements:
            anonymous_applications = announcement.anonymous_applications.all().count()
            candidate_applications = Postulacion.objects.filter(announcement=announcement).count()
            apply_count.append(anonymous_applications + candidate_applications)
        context['all_job_offers'] = zip(announcements,apply_count)
        context['today'] = timezone.now()
        return context

@method_decorator(business_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class JobOfferDetailView(DetailView):
    model = Convocatoria
    template_name = 'convocatoria/job_offer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcement = Convocatoria.objects.get(pk=self.kwargs['pk'])
        context['applications'] = Postulacion.objects.filter(announcement=self.kwargs['pk'])
        context['anonymous_applicants'] = announcement.anonymous_applications.all()
        return context

@method_decorator(candidate_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AllCandidateJobOffersListView(ListView):
    model = Postulacion
    template_name = 'convocatoria/all_candidate_job_offers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_applications'] = Postulacion.objects.filter(candidate=self.request.user)
        context['today'] = timezone.now()
        return context

@method_decorator(candidate_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class CandidateApplyJobOfferView(View):
    def get(self, request, **kwargs):
        announcement = Convocatoria.objects.get(pk=kwargs['pk'])
        #Se verifica si ya expiró
        if(timezone.now() >= announcement.closing_date_time or announcement.status != "1"):
            messages.error(request, 'La oferta ha terminado')
        #Si no ha expirado
        else:
            #se busca si existe una postulación
            apply_object = Postulacion.objects.filter(announcement=kwargs['pk'], candidate=self.request.user)
            #Si no se ha postulado anteriormente
            if apply_object.count() < 1:
                # se crea una nueva instancia y se guarda
                postulacion = Postulacion.objects.create(candidate=self.request.user, announcement=announcement)
                postulacion.save()
                #Se asocia a la convocatoria
                messages.success(request, 'Postulacion exitosa')
            else:
                messages.error(request, 'Usted ya se ha postulado con anterioridad')
        return redirect('/')