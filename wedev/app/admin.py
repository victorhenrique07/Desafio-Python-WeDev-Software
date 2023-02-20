from django.contrib import admin
from app.models import Telefone, Curso, Aluno, Professor, EntidadeAssociativa
from django.contrib.auth.admin import UserAdmin

    
class TelefoneInline(admin.TabularInline):
    model = Telefone
    
class EntidadeInline(admin.TabularInline):
    model = EntidadeAssociativa

class CursoInline(admin.TabularInline):
    model = Curso
    
class AlunoAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline, EntidadeInline]
    
class ProfessorAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]
    
#


# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
