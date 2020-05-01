from django.urls import path
from .views import ( CreateJobOfferView, AllJobOffersListView, 
JobOfferDetailView, AllCompanyJobOffersListView, 
AnonymousApplyJobOfferView, AllCandidateJobOffersListView,
CandidateApplyJobOfferView )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AllJobOffersListView.as_view(), name='convocatoria.convocatorias'),
    path('aplicarVisitante/<int:pk>', AnonymousApplyJobOfferView.as_view(), name='convocatoria.aplicarAnonimo'),
    path('aspirante/Aplicar/<int:pk>', CandidateApplyJobOfferView.as_view(), name='convocatoria.aplicarAspirante'),
    path('crearConvocatoria', CreateJobOfferView.as_view(), name='convocatoria.crear'),
    path('misConvocatorias', AllCompanyJobOffersListView.as_view(), name='convocatoria.listar'),
    path('convocatoria/<int:pk>', JobOfferDetailView.as_view(), name='convocatoria.detalles'),
    path('aspirante/misConvocatorias', AllCandidateJobOffersListView.as_view(), name='convocatoria.listarAspirante'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)