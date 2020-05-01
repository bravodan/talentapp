from graphene import ObjectType, String, Schema
from .convocatoria_schema import Query as ConvocatoriaQuery, Mutation as ConvocatoriaMutation
from .auth_schema import Mutation as AuthMutation

class Query(ConvocatoriaQuery):
    pass   

class Mutation(ConvocatoriaMutation, AuthMutation):
    pass

ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)