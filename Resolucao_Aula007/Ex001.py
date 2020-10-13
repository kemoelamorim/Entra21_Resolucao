""" 
--- Exercício 1  - Funções - 1
--- Escreva uma função que imprima um cabeçalho
--- O cabeçalho deve ser escrito usando a multiplicação de carácter
--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
--- Realize a chamada da função na ultima linha do seu programa 
"""
empresa = input('Digite o nome da empesa: ')

def cabecalho(empresa):
    print(f"{empresa:*^30}".upper() )

cabecalho(empresa)