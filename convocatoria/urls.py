from django.urls import path
from .views import CreateJobOfferView, AllJobOffersListView, JobOfferDetailView

urlpatterns = [
    path('crearConvocatoria', CreateJobOfferView.as_view(), name='convocatoria.crear'),
    path('misConvocatorias', AllJobOffersListView.as_view(), name='convocatoria.listar'),
    path('convocatoria/<int:pk>', JobOfferDetailView.as_view(), name='convocatoria.detalles'),
]