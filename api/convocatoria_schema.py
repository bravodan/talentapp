from graphene_django import DjangoObjectType
from convocatoria.models import Convocatoria as ConvocatoriaModel
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from convocatoria.forms import JobOfferForm
import graphene
from graphql_jwt.decorators import login_required

class Convocatoria(DjangoObjectType):
    """ Nodo del grafo """
    class Meta:
        model = ConvocatoriaModel
        filter_fields = {
            'job_title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'closing_date_time': ['gt', 'gte', 'lt', 'lte'],
            'created_at': ['gt', 'gte', 'lt', 'lte'],
            'status':['exact']
        }
        interfaces = (relay.Node,)
        exclude = ['company',]

class Query(ObjectType):
    convocatoria = relay.Node.Field(Convocatoria)

    @login_required
    def resolve_convocatoria(self, info, *args, **kwargs):
        return ConvocatoriaModel.objects.filter(**kwargs)

class ConvocatoriaMutation(DjangoModelFormMutation):
    class Meta:
        form_class =JobOfferForm

class Mutation(ObjectType):
    crear_convocatoria = ConvocatoriaMutation.Field()

    @login_required
    def resolve_crear_convocatoria(self, info, *args, **kwargs):
        return ConvocatoriaModel.objects.filter(**kwargs)