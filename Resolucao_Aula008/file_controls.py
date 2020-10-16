# Cria e Manipula aquivos de Texto

# x = cria um novo arquivo, caso o arquivo ja exista, da erro
def cria_newFile(pessoa):
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','x')
    arquivo.write(f"{pessoa['nome']};{pessoa['sobrenome']};{pessoa['idade']};{pessoa['i_d']} ")
    arquivo.close()
    return 'Primeiro Cadastro salvo'

# w = cria um novo arquivo, porem se o arquivo existir ele apaga o antigo
def criar_e_substituiFile(pessoa):
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','w')
    arquivo.write(f"{pessoa['nome']};{pessoa['sobrenome']};{pessoa['idade']};{pessoa['i_d']} ")
    arquivo.close()
    return 'Criou e subistituiu cadastro'

# a = adiciona uma nova linha ao final do arquivo
def add_File(pessoa):
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','a')
    arquivo.write(f"{pessoa['nome']};{pessoa['sobrenome']};{pessoa['idade']};{pessoa['i_d']} ")
    arquivo.close()
    return 'Cadastro adicionado e salvo'

# leitura de arquivo
def writeFile(pessoa):
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','r')
    for linha in arquivo:
        return linha
    arquivo.close()