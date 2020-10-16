# Cria e Manipula aquivos de Texto

# x = cria um novo arquivo, caso o arquivo ja exista, da erro
def cria_newFile():
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','x')
    arquivo.write('Primeiro arquivo')
    arquivo.close()

# w = cria um novo arquivo, porem se o arquivo existir ele apaga o antigo
def criar_e_substituiFile():
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','w')
    arquivo.write('Criou e subistituiu..')
    arquivo.close()

#-- a = adiciona uma nova linha ao final do arquivo
def add_File():
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','a')
    arquivo.write('Adicionou ao arquivo..')
    arquivo.close()

# leitura de arquivo
def writeFile():
    arquivo = open('Resolucao_Aula008/files/pessoa.txt','r')
    for linha in arquivo:
        return linha
    arquivo.close()