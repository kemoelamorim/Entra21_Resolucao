""" 
--- Exercício 5 - Funções
--- Crie uma função para calculo de raiz
--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
--- Leia um número do console, armazene em uma variável e passe para a função
--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
--- Imprima o resultado e uma mensagem usando f-string, fora da função 
"""

def caucula_raiz(numero, indice):
    raiz = numero ** (1 / indice)
    return raiz

numero = int(input('Digite um numero: '))
indice = int(input('Digite o indice: '))
raiz = caucula_raiz(numero, indice)
print(f'A raiz entre o indice {indice} e o numero {numero} é igual a %.0f' % raiz)
