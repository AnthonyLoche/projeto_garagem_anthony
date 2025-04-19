from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=False, blank=False)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, null=False, blank=False)
    acessorios = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"ID: {self.id} - Modelo: {self.modelo} - Cor: {self.cor} - Ano: {self.ano}"
    
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['modelo', 'cor', 'ano']