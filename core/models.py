from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()
    fone = models.CharField(max_length=11)
    email = models.EmailField()
    data_registro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='pet')
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'

    