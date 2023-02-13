from django.contrib import admin
from app.models import Telefone, Curso, Aluno, Professor, EntidadeAssociativa


class TelefoneAdmin(admin.TabularInline):

    model = Telefone

class EntidadeAdmin(admin.TabularInline):

    model = EntidadeAssociativa

class AlunoAdmin(admin.ModelAdmin):
    
    inlines = [TelefoneAdmin, EntidadeAdmin]
    
class ProfessorAdmin(admin.ModelAdmin):
    
    inlines = [TelefoneAdmin]
    



# Register your models here.

admin.site.register(Curso)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)