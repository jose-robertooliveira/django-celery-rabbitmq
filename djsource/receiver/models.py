from django.db import models
#from django.contrib.auth.models import User


class Proposta(models.Model):
    STATUS_CHOICES = (
        ('Negada', 'Negada'),
        ('Aprovada', 'Aprovada'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Negada')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    valor_emprestimo = models.DecimalField(max_digits=20, decimal_places=2)
    # outros campos da proposta...


# class Cadastro(models.Model):
#     nome = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=50)
#     endereco = models.CharField(max_length=100)
#     valor_emprestimo = models.DecimalField(max_digits=20, decimal_places=2)
