""" 
--- Exercício 1  - Funções
--- Escreva uma função para cadastro de pessoa:
---       a função deve receber três parâmetros, nome, sobrenome e idade
---       a função deve salvar os dados da pessoa em uma lista com escopo global
---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
---       A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada 
"""


#=== escopo global
cadastros = []

def cadastrar(nome, sobrenome, idade):
    
    if idade < 18:
        print("Idade não permitida!")
       
    
    else:
        pessoa = {'nome': nome,'sobrenome': sobrenome,'idade': idade}
        pessoa['i_d'] = len(cadastros) + 1
        cadastros.append(pessoa)
        print("Pessoas cadrastradas!")
        return cadastros


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

cadrastros = cadastrar(nome, sobrenome, idade)

#-- Escrita
dict_person = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade}
arquivo = open('pessoa.txt','a')
arquivo.write(f"{dict_person['nome']};{dict_person['sobrenome']};{dict_person['idade']}; \n")
arquivo.close()

#-- Leitura
cadastros = open('pessoa.txt','r')
for linha in cadastros:
    linha_limpa = linha.strip() #-- limpa espaços em brando e caracteres de formatação (\n \t)
    lista_dados = linha_limpa.split(';')
    print(f"nome:{lista_dados[0]} - sobrenome:{lista_dados[1]}, idade:{lista_dados[2]}")

arquivo.close()

for cadastro in cadastros:
    print(cadastro)
