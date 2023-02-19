from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    TIPO_PESSOA = [
        ('aluno', 'Aluno'), 
        ('professor', 'Professor')
    ]    
    
    type = models.CharField(max_length=9, editable=True, blank=False, null=False, choices=TIPO_PESSOA)
    state = models.CharField(max_length=2, editable=True, blank=True, null=False)
    city = models.CharField(max_length=30, editable=True, blank=True, null=False)
    address = models.CharField(max_length=70, editable=True, blank=True, null=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return "%s %s %s" % (self.state, self.city, self.address)
    
class Curso(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=80, editable=True, blank=False, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s %s %s" % (
            self.active,
            self.name,
            self.start_date,
            self.finish_date,
        )


class Infos(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=255)