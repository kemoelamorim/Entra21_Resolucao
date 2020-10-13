""" 
--- Exercício 3  - Funções
--- Crie uma função que leia três números float
--- Armazene cada valor lido em uma variável
--- Calcule a média entre os três números e armazene em uma quarta variável
--- Imprima a média e uma mensagem usando f-string (módulo 3) 
"""

a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

def calcula_media(a,b,c):
    media = (a + b + c )/3
    return print(f'A média entre os numeros {a} {b} e {c} é igual a %.3f' % media)

calcula_media(a,b,c)