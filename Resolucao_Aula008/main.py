from funcoes import cadastrar_pessoa,  listar_pessoas_cadastradas, pessoas, pessoa_especifica
from funcoes import cadastrar_endereco, listar_enderecos_cadastrados, enderecos, endereco_especifico
from file_controls import*

# Dados para o cadastro de Pessoas
print('Cadastrando pessoas')
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

pessoa = cadastrar_pessoa(nome, sobrenome, idade)

# Dados para o cadastro de Endereços
i_d = (len(pessoas))# ((pessoa['i_d'])for pessoa in pessoas)
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

# manipulação de arquivos
print(""" 
O que deseja fazer com cadastros?
1 - Primeiro cadastro 
2 - Adicionando e Salvando
3 - Salvar e Substituir
4 - Ver cadastros salvos
""")
escolha_menu = input('Digite a opção Desejada?: ')

if escolha_menu == '1':
    status = cria_newFile(pessoa)
    print(status)
elif escolha_menu == '2':
    status = add_File(pessoa)
    print(status)
elif escolha_menu == '3':        
    status = criar_e_substituiFile(pessoa)
    print(status)
elif escolha_menu == '4':
    status = writeFile(pessoa)
    print(status)
else:
    print('tchau')