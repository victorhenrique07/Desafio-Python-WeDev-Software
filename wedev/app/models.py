from django.db import models


# Create your models here.
class Informacao(models.Model):
    aluno = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)
    name = models.CharField(max_length=55, editable=True, blank=False, null=False)
    lastname = models.CharField(max_length=55, editable=True, blank=False, null=False)
    email = models.EmailField(max_length=70, editable=True, blank=False, null=False)
    state = models.CharField(max_length=2, editable=True, blank=False, null=False)
    city = models.CharField(max_length=30, editable=True, blank=False, null=False)
    address = models.CharField(max_length=70, editable=True, blank=False, null=False)
    username = models.CharField(max_length=20, editable=True, blank=False, null=False)
    password = models.CharField(max_length=26, editable=True, blank=False, null=False)
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" % (
            self.id,
            self.aluno,
            self.professor,
            self.name,
            self.lastname,
            self.email,
            self.state,
            self.city,
            self.address
        )


class Telefone(models.Model):
    name = models.ForeignKey(Informacao, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=255, editable=True, blank=False, null=False)
    
    def __str__(self):
        return "%s %s" % (self.name, self.telefone)

class Curso(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=80, editable=True, blank=False, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    professor = models.ForeignKey(Informacao, on_delete=models.CASCADE, verbose_name="professor do curso")
#
    
class AssociacaoUsuariosInforCurso(models.Model):
    usuario = models.ForeignKey(Informacao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
