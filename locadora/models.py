from django.db import models
from django.conf import settings

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=25)

    def __str__(self):
        return self.nome 

class Veiculo(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='locadora/media', blank=True)
    descricao = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nome 

class Locacao(models.Model):
    descricao = models.CharField(max_length=200)
    cliente = models.ManyToManyField(Cliente, blank = True) #relacionamento m-n muito-para-muitos
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veiculo") #relacionamento 1-n
    placa = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    #python -m pip install Pillow
    periodo = models.IntegerField()

    def __str__(self):
        return self.descricao