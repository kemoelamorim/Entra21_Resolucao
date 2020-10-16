from funcoes import cadastrar_pessoa,  listar_pessoas_cadastradas, pessoas, pessoa_especifica
from funcoes import cadastrar_endereco, listar_enderecos_cadastrados, enderecos, endereco_especifico

# Dados para o cadastro de Pessoas
print('Cadastrando pessoas')
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

cadastro = cadastrar_pessoa(nome, sobrenome, idade)

# Dados para o cadastro de Endereços
i_d = len(cadastro)  # Passando o i_d da pessoa 
rua = input('Digite sua rua: ')
numero = input('Digite seu numero: ')
complemento = input('Digite o complemento: ')
bairro = input('Digite o seu bairro: ')
cidade = input('Digite a sua cidade: ')
estado = input('Digite seu Estado: ')

endereco = cadastrar_endereco(i_d, rua, numero, complemento, bairro, cidade, estado)

# Listar Pessoas
dictPessoas = listar_pessoas_cadastradas(pessoas)
print(dictPessoas)

# Buscas Pessoa específica
buscaPessoa = int(input('Buscar pessoa por ID: '))
pessoaEspecifia = pessoa_especifica(buscaPessoa)
print(pessoaEspecifia)
# Listar Endereços
dictEnderecos = listar_enderecos_cadastrados(enderecos)
print(dictEnderecos)

# Busca endereço especifico
buscaEndereco = int(input('Buscar endereço por ID: '))
enderecoEspecifico = endereco_especifico(buscaEndereco)
print(enderecoEspecifico)