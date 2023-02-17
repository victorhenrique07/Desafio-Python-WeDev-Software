from django.contrib import admin
from app.models import Infos, Curso, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
    
class InfosAdmin(admin.TabularInline):
    model = Infos
    
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = [InfosAdmin]
    list_display = ['username', 'email', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'state', 'city', 'address', 'type')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('state', 'city', 'address')}),
    )


# Register your models here.
admin.site.register(Curso)
admin.site.register(Infos)
admin.site.register(CustomUser, CustomUserAdmin)
