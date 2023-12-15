from django.shortcuts import render
from django.http import HttpResponse

from .utils import valida_cpf
from .utils import remove_caracteres_especiais


def validar_cpf(request):
    mensagem = None 

    if request.method == 'POST':
        cpf_digitado = request.POST.get('cpf')
        cpf_numeros = [int(digito) for digito in cpf_digitado if digito.isdigit()]

        if len(cpf_numeros) == 11 and len(set(cpf_numeros)) !=1:
            resultado = valida_cpf(cpf_numeros)

            if resultado:
                mensagem = 'CPF É VÁLIDO'
            else:
                mensagem = 'CPF NÃO É VÁLIDO'
        else:
            mensagem = 'Os números estão repetidos e/ou possui dados invalidos'

    return render(request, 'brutus/validar_cpf.html', {'mensagem': mensagem})

def remove_caracteres_especiaiss(request):
    if request.method == 'POST':
        frase = request.POST.get('fraseDig')
        resultadoF = remove_caracteres_especiais(frase)
        return render(request, 'brutus/validar_cpf.html', {'resultadoF': resultadoF})
    else:
        return render(request, 'brutus/validar_cpf.html') 