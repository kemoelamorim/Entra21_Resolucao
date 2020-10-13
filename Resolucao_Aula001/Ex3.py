""" 
--- Exercício 3  - Variáveis
--- Imprima dois parágrafos do último livro que você leu
--- A impressão deve conter informações do livro, que deverão estar em variáveis
--- As informações do Livro serão: 
---    Título
---    Edição
---    Autor
---    Data de publicação
--- Os parágrafos devem estar formatados conforme a formatação do livro
"""

titulo = 'PensePython'
edicao = '2e'
autor = 'Allen B. Downey'
data_publicacao = 'Abril 2002' 

primeiro_paragrafo = """ Um dicionário contém uma coleção de índices, que se chamam chaves e uma coleção de valores.\nCada chave é associada com um único valor. A associação de uma chave e um valor chama-se par chave-valor ou item. """

segundo_paragrafo = """ A função dict cria um novo dicionário sem itens. Como dict é o nome de uma função integrada, você\ndeve evitar usá-lo como nome de variável. """

print(f'''
Titulo: {titulo}
Edição: {edicao}
Autor: {autor}
Data de publicação: {data_publicacao}

Primeiro Paragrafo: {primeiro_paragrafo}

Segundo Paragrafo: {segundo_paragrafo}
''')