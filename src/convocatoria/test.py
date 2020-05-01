from django.test import TestCase
from usuario.models import Usuario

class createCustomUserTestCase(TestCase):
    def setUp(self):
        #datos para los usuarios
        self.users_data = [["usuario5@usuario.com", "usuariosistema",  "Namtrik", "Namtrik", "Development", True, False],
            ["usuario6@usuario.com", "usuariosistema", "Namtrik", "Namtrik", "Development", False, True],
            ["usuario8@usuario.com", "usuariosistema", "Usuario", "Usuario", "8", False, True]]
        #creacion y guardado de usuarios
        for user in self.users_data:
            user_created = Usuario.objects.create_user(email=user[0],password=user[1], username=user[2],first_name=user[3],last_name=user[4],is_business_user=user[5], is_candidate_user=user[6])
            user_created.save()

    def test_custom_user_created(self):
        #Se obtienen todos los usuarios en la base de datos
        usuarios = Usuario.objects.all()
        #se compara si los atributos de los usuarios creados son iguales a los campos ingresados
        for usuario, user in zip(usuarios, self.users_data):
            self.assertTrue(usuario.email == user[0])
            self.assertTrue(usuario.username == user[2])
            self.assertTrue(usuario.first_name == user[3])
            self.assertTrue(usuario.last_name == user[4])
            self.assertTrue(usuario.is_business_user == user[5])
            self.assertTrue(usuario.is_candidate_user == user[6])
        