""" 
--- Exercício 2  - Funções
--- Escreva uma função que leia dois números do console
--- Armazene cada número em uma variável
--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
--- Imprima o resultado e uma mensagem usando f-string 
"""

def ler_dois_numeros():
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    if b != 0:
        divisao = a / b
    return print(f'A divisão entre {a} e {b} é igual a %.2f' % divisao)

ler_dois_numeros()
