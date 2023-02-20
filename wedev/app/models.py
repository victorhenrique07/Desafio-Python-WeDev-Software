from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=70, editable=True, blank=True, null=False)
    last_name = models.CharField(max_length=70, editable=True, blank=True, null=False)
    email = models.EmailField(max_length=40, editable=True, blank=True, null=False)
    state = models.CharField(max_length=2, editable=True, blank=True, null=False)
    city = models.CharField(max_length=30, editable=True, blank=True, null=False)
    address = models.CharField(max_length=70, editable=True, blank=True, null=False)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (
            self.user, self.name, self.last_name, self.email, self.state, self.city, self.address
            )
    
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, editable=True, blank=True, null=False)
    last_name = models.CharField(max_length=70, editable=True, blank=True, null=False)
    email = models.EmailField(max_length=40, editable=True, blank=True, null=False)
    state = models.CharField(max_length=2, editable=True, blank=True, null=False)
    city = models.CharField(max_length=30, editable=True, blank=True, null=False)
    address = models.CharField(max_length=70, editable=True, blank=True, null=False)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"


class Curso(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=80, editable=True, blank=False, null=False)
    start_date = models.DateField()
    finish_date = models.DateField()
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, verbose_name="professor do curso"
    )

    def __str__(self):
        return "%s %s %s %s %s" % (
            self.active,
            self.name,
            self.start_date,
            self.finish_date,
            self.professor,
        )


class Telefone(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.telefone)


class EntidadeAssociativa(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
