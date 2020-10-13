"""
--- Exercício 2  - Variáveis
--- Crie um menu para um sistema de cadastro de funcionários
--- O menu deve ser impresso com a função format()
--- As opções devem ser variáveis do tipo inteiro
--- As descrições das opções serão:
---    Cadastrar funcionário
---    Listar funcionários
---    Editar funcionário
---    Deletar funcionário
---    Sair
--- Além das opções o menu deve conter um cabeçalho e um rodapé
--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação
"""

# Criando Menu
print(f"{'Cadastro de funcionário':=^30}\n\n\n".upper())
print("""Menu - Escolha uma das opções:
1 Cadastrar funcionário
2 Listar funcionários
3 Editar funcionário
4 Deletar funcionário
5 Sair
""")

opcao = int(input("Digite a opção desejada: "))

if(opcao == 1):
    print(f"{'Cadastrar funcionário':=^30}\n\n\n".upper())
    print(f"{'fim':=^30}".upper())

elif(opcao == 2):
    print(f"{'Listar funcionários':=^30}\n\n\n".upper())
    print(f"{'fim':=^30}".upper())

elif(opcao == 3):
    print(f"{'Editar funcionário':=^30}\n\n\n".upper())
    print(f"{'fim':=^30}".upper())

elif(opcao == 4):
    print(f"{'Deletar funcionário':=^30}\n\n\n".upper())
    print(f"{'fim':=^30}".upper())

elif(opcao == 5):
    print(f"{'Sair':=^30}\n\n\n".upper())
    print(f"{'fim':=^30}".upper())

else:
    print("""
    Você deve escolher uma das opções:
    1 Cadastrar funcionário
    2 Listar funcionários
    3 Editar funcionário
    4 Deletar funcionário
    5 Sair""")