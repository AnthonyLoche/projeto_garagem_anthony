from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"ID: {self.id} - Nome: {self.nome}"
    
    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        ordering = ['nome']