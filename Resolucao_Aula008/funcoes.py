# Exercício 1
pessoas = []
def cadastrar_pessoa(nome, sobrenome, idade):
    
    if idade < 18:
        print("Idade não permitida!")
    
    else:
        pessoa = {'nome': nome,'sobrenome': sobrenome,'idade': idade}
        pessoa['i_d'] = len(pessoas) + 1
        pessoas.append(pessoa)
        print("Pessoa cadastrada!")
        return pessoas

# Exercício 2
enderecos = []  
def cadastrar_endereco(i_d, rua, numero, complemento, bairro, cidade, estado):
    endereco = {'rua': rua,'numero': numero,'complemento': complemento,'bairro': bairro,
    'cidade': cidade,'estado': estado,'i_d': i_d}
    enderecos.append(endereco)

    for chave, valor in endereco.items():
        if chave == None or valor == '':
            print('Valores não preenchidos!')
        else: 
            print('Endereço realizado com sucesso')
        return enderecos

# Exercício 3
def listar_pessoas_cadastradas(pessoas):
    print(f'Quanditade de pessoas cadastradas: {len(pessoas)}')
    for pessoa in pessoas:
        return pessoa
# Buscando pessoa por ID
def pessoa_especifica(buscaPessoa):
    for pessoa in pessoas:
        if pessoa['i_d'] == buscaPessoa:
            return pessoa

# Exercício 4
def listar_enderecos_cadastrados(enderecos):
    print(f'Quanditade de endereços cadastrados: {len(enderecos)}')
    for endereco in enderecos:
        return endereco
# Buscando endereço por ID
def endereco_especifico(buscaEndereco):
    for endereco in enderecos:
        if endereco['i_d'] == buscaEndereco:
            return endereco

