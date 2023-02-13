from django.db import models


# Create your models here.
class Pessoa(models.Model):
    name = models.CharField(max_length=55, editable=True, blank=False, null=False)
    lastname = models.CharField(max_length=55, editable=True, blank=False, null=False)
    email = models.EmailField(max_length=70, editable=True, blank=False, null=False)
    state = models.CharField(max_length=2, editable=True, blank=False, null=False)
    city = models.CharField(max_length=30, editable=True, blank=False, null=False)
    address = models.CharField(max_length=70, editable=True, blank=False, null=False)
    username = models.CharField(max_length=20, editable=True, blank=False, null=False)
    password = models.CharField(max_length=26, editable=True, blank=False, null=False)
    
class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass


class Telefone(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='telefones', null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='telefones', null=True)
    telefone = models.CharField(max_length=255)
    
class Curso(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=80, editable=True, blank=False, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="professor do curso")
#
class EntidadeAssociativa(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)