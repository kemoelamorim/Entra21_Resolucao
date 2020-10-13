""" 
--- Exercício 4  - Funções
--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
--- A impressão deve ocorrer via multiplicação de strings
--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
--- Crie uma chamada para as duas função, para exibir o resultado no console 
"""



class Funcao:

    def __init__(self, cabecalho, rodape):
        self._cabecalho = cabecalho

    def __str__(self):
        return f"{cabecalho:*^30}\n{rodape:*^30}".upper() 

cabecalho = input('Digite o nome da empesa: ')
rodape = 'fim' 

funcao = Funcao(cabecalho,rodape)
print(funcao)
