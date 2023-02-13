from django.contrib import admin
from app.models import Usuario, Telefone, Curso, Aluno, AssociacaoAlunoUsuario


class TelefoneAdmin(admin.TabularInline):
    model = Telefone


class UsuarioAdmin(admin.ModelAdmin):
    
    inlines = [TelefoneAdmin,]
    

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Telefone)
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(AssociacaoAlunoUsuario)