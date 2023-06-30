from django.contrib import admin
from .models import Proposta


class PropostaAdmin(admin.ModelAdmin):
    fields = ('nome', 'cpf', 'endereco', 'valor_emprestimo')
    list_display = ('nome', 'valor_emprestimo')

admin.site.register(Proposta, PropostaAdmin)
