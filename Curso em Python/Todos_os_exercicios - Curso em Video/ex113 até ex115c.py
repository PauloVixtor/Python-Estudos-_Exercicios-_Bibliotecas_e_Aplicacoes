### Desafio 113 ### -

# Rescreva a função leiaint() que dizemos no exercicio 104.
#  incluindo agora possibilidade da digitação de um tipo invalido
# Aproveite e crie uma função leiafloat() com mesma funcionalidade

"""
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número valido.\033[m')
        else:
            break
    return n


def leiafloat(msg2):
    while True:
        try:
            m = float(input(msg2))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número valido.\033[m')
        except KeyboardInterrupt:
            print('O Usuario preferiu não informar dados!')
        else:
            break
    return m


x = leiaint('Digite um número inteiro: ')
y = leiafloat('Digite um número real: ')"""
# print(f'O valor inteiro digitado foi {x}, e o valor real {y}')


### Desafio 114 ### - Revisão

# Crie um codigo em Python que teste se o site pudim está acessivel pelo computador.

"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com')
except:
    print('\033[1;95mO site não está acessivel no momento!\033[0;0m')
else:
    print('\033[1;32mConsegui acessar o site com sucesso!\033[0;0m')"""




### Desafio 115 ### -

# Crie um pequeno sistema de modularização que permita cadastrar pessoas pelo seu nome.
# E idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastrar.

"""
from Cadastrar import leiastr, leiaint

dados = []

while True:
    inserir = []
    print('-' * 30)
    print('        MENU PRINCIPAL')
    print('-' * 30)
    print('\033[1;33m1 -\033[1;34m Ver pessoas cadastradas\033[0;0m')
    print('\033[1;33m2 -\033[1;34m Cadastrar nova pessoa\033[0;0m')
    print('\033[1;33m3 -\033[1;34m Sair do sistema\033[0;0m')
    print('-' * 30)
    opcao = leiaint('Sua opção: ')
    while opcao < 1 or opcao > 3:
        print(f'{opcao} invalida. Escolha novamente!')
        opcao = leiaint('Sua opção: ')
    if opcao == 1:
        print('-' * 30)
        print('     PESSOAS CADASTRADAS')
        print('-' * 30)
        for c in range(0, len(dados)):
            print(f'  {dados[c][0]:>5}', end='      ')
            print(f'  {dados[c][1]} anos')
    elif opcao == 2:
        nome = leiastr('Nome: ')
        inserir.append(nome)
        idade = leiaint('Idade: ')
        inserir.append(idade)
        dados.append(inserir)
        print(f'Novo registro de {nome} adicionado.')
    elif opcao == 3:
        print('-' * 30)
        print('      SAINDO DO SISTEMA')
        print('-' * 30)
        break"""