""" --- Exercício 5  - Funções
--- Escreva um programa para cadastro de pessoas e endereços:
---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
---       o programa deve solicitar os dados de endereços utilizados na função do ex2
---       o programa deve passar o id obtido na função do ex1 para a função do ex2
---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
                com seus respectivos endereços utilizando as funções do ex3 e ex4 
"""

from cadastrando_pessoas import cadastrar_pessoas,pessoas
from cadastrando_endereco import cadastrar_enderecos,enderecos

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

cadrastros = cadastrar_pessoas(nome, sobrenome, idade)

for cadastro in pessoas:
    print(cadastro)

i_d = len(pessoas) + 1
rua = input('Digite sua rua: ')
numero = input('Digite seu numero: ')
complemento = input('Digite o complemento: ')
bairro = input('Digite o seu bairro: ')
cidade = input('Digite a sua cidade: ')
estado = input('Digite seu Estado: ')

cadastrar_enderecos(i_d, rua, numero, complemento, bairro, cidade, estado)

for endereco in enderecos:
    print(enderecos)
