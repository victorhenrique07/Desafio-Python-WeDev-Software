from django.db import models


# Create your models here.
class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    aluno = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)
    name = models.CharField(max_length=55, editable=True, blank=False, null=False)
    lastname = models.CharField(max_length=55, editable=True, blank=False, null=False)
    email = models.EmailField(max_length=70, editable=True, blank=False, null=False)
    state = models.CharField(max_length=2, editable=True, blank=False, null=False)
    city = models.CharField(max_length=30, editable=True, blank=False, null=False)
    address = models.CharField(max_length=70, editable=True, blank=False, null=False)
    
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
    name = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=255, editable=True, blank=False, null=False)
    
    def __str__(self):
        return "%s %s" % (self.name, self.telefone)

class Curso(models.Model):
    name = models.CharField(max_length=80, editable=False, blank=False, null=False)
    active = models.BooleanField()
    start_date = models.DateField()
    finish_date = models.DateField()
    professor = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="professor do curso")

    def __str__(self):
        return "%s %s %s %s %s" % (
            self.name,
            self.active,
            self.start_date,
            self.finish_date,
            self.professor,
        )
        
class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, editable=False, blank=False, null=False)
    password = models.CharField(max_length=26, editable=True, blank=False, null=False)
    
class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, editable=False, blank=False, null=False)
    password = models.CharField(max_length=26, editable=True, blank=False, null=False)
    
class AssociacaoProfessorCurso():
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class AssociacaoAlunoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

