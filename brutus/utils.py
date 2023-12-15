# VALIDA CPF

def valida_cpf(listaA):
    """
    Valida se o CPF digitado é válido ou não.

    Parâmetros:
    - listaA: Números do CPF em uma lista de inteiros.

    Retorno:
    - Informa se o CPF é válido ou não.
    """
    resultados_lista_um = []
    resultados_lista_dois = []
    calc = 10
    calc_dois = 11

    for i in range(len(listaA)):
        if i <= 8:
            resultado = listaA[i] * calc
            resultados_lista_um.append(resultado)
            calc = calc - 1

    soma_resultados_lista_um = sum(resultados_lista_um)
    resto_div_onze = soma_resultados_lista_um % 11

    if resto_div_onze < 2:
        digito_um = 0
    else:
        digito_um = 11 - resto_div_onze

    for i in range(len(listaA)):
        if i <= 9:
            resultado_dois = listaA[i] * calc_dois
            resultados_lista_dois.append(resultado_dois)
            calc_dois = calc_dois - 1

    soma_resultados_lista_dois = sum(resultados_lista_dois)
    div_dois = soma_resultados_lista_dois % 11

    if div_dois < 2:
        digito_dois = 0
    else:
        digito_dois = 11 - div_dois

    verificador = [digito_um, digito_dois]

    if listaA[9] == verificador[0] and listaA[10] == verificador[1]:
        return True
    else:
        return False

# REMOVE CARACTER
def remove_caracteres_especiais(frase):
    """
    Remove os caracteres de uma string, os espaços do final e do inicio do texto
    
    parametros: string com caractreres especiais
    retorno: string sem caracteres especiais
    """
    frase_sem_especiais = ''.join(caracter for caracter in frase if caracter.isalnum() or caracter.isspace())
    frase_sem_especiais = ' '.join(frase_sem_especiais.split())
    print('Frase sem os caracteres especiais: ', frase_sem_especiais,'\n')

    return frase_sem_especiais