from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import Proposta
import random


@shared_task
def analisar_propostas():
    propostas = Proposta.objects.all()

    # Define a quantidade de propostas a serem aprovadas
    aprovadas_count = propostas.count() // 2

    # Randomiza as propostas a serem aprovadas
    propostas_aprovadas = random.sample(list(propostas), aprovadas_count)

    # Atualiza o status das propostas
    for p in propostas:
        status = 'Negada'
        if p in propostas_aprovadas:
            status = 'Aprovada'
        p.status = status
        p.save()

