from django.contrib import admin
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('email', 'username',  'first_name', 'last_name', 'is_staff',)
    list_filter = ('is_staff',)
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('username',)

admin.site.register(Usuario, CustomUserAdmin)