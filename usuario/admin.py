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
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'is_candidate_user', 'is_business_user')}
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username',)
    ordering = ('username',)

admin.site.register(Usuario, CustomUserAdmin)