from django.contrib import admin
from app.models import Informacao, Telefone, Curso, AssociacaoUsuariosInforCurso


class TelefoneAdmin(admin.TabularInline):
    model = Telefone


class InformacaoAdmin(admin.ModelAdmin):
    
    inlines = [TelefoneAdmin,]

# Register your models here.

admin.site.register(Informacao,InformacaoAdmin)
admin.site.register(Telefone)
admin.site.register(Curso)
admin.site.register(AssociacaoUsuariosInforCurso)
