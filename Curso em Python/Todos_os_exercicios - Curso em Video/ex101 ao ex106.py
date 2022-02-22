### Desafio 101 ### - Correto

# Crie um programa que tenha uma função chamada voto()
# Que vai receber cmo parametro: ano de nascimento de uma pessoa
# Retonrnado um valor literal se uma pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATORIA nas eleições

"""
def voto(ano_nasc):
    ""
    -> Analisa o ano de nascimento de uma pessoa e retorna se pessoa precisa votar.
    :param ano_nasc: Ano de Nascimento.
    :return: Retorna OBRIGATORIO, OPCIONAL OU NÃO VOTA.
    ""
    from datetime import date

    atual = date.today().year
    eleitor = atual - ano_nasc
    if eleitor >= 18 and eleitor < 65:
        return (f'Com {eleitor} anos: VOTO OBRIGATORIO.')
    elif eleitor < 16:
        return (f'Com {eleitor} anos: NÃO VOTA.')
    elif eleitor >= 16 and eleitor < 18 or eleitor >= 65:
        return (f'Com {eleitor} anos: VOTO OPCIONAL.')

help(voto)
print('-' * 30)
ano = int(input('Digite ano de nascimento: '))
print(voto(ano))"""

### Desafio 102 ### - Correto

# Crie um programa que crie uma função factorial que recebe dois parametros
# O primeiro que indique o numero a calcular
# E o outro chamado show que será um valor logico (opcinal)
# Indicando se será mostado ou não, na tela o valor de fatorial.

"""
lista = list()

def fatorial(num, show=False):
    ""
    --> Calcula fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número n.
    ""
    f = 1
    for c in range(num, 0, -1):
        lista.append(c)
        f *= c
    conta = str(lista).replace(',', ' x ').replace(']', ' = ').replace('[', '')
    if show == False:
        return f
    elif show == True:
        return (f'{conta}{f}')

n = int(input('Digite o valor: '))
print('=' * 26)
mostrar = int(input('--> Deseja Mostrar na tela?\n'
                    '==========================\n'
                    '-> Mostrar na tela     [1]\n'
                    '-> Não mostrar na tela [2]\n'
                    '-------------------------\n'
                    'Escolhe uma opção: '))
while mostrar > 2 or mostrar < 1:
    mostrar = int(input('Resposta invalida. Digite um número valido: '))
if mostrar == 1:
    print('-' * 26)
    print(fatorial(n, show=True))
else:
    print('-' * 26)
    print(fatorial(n, show=False))
print('\n')
help(fatorial)"""

### Desafio 103 ### - Revisado

# Faça um programa que tenha uma função chamada ficha()
# Que recebe parametros opcionais nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum daod não tenha sido informado corretamente.

"""
def ficha(jogadors='', gols=0):
    global jogador
    if jogador == '':
        jogadors = '<Desconhecido>'
    return f'O jogador {jogadors} fez {gols} no campeonato'
jogador = str(input('Nome do jogador: '))
gol = input('Número de Gols: ')
if gol == '' or gol == str():
    gol = 0

print(ficha(jogador, gols=gol))
"""

# Revisão

"""
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato')

n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)"""

### Desafio 104 ### - Revisado

# Crie um programa que tenha a função leiaint()
# Que vai funcionar semelhante a função input() no python
# Só que fazendo a validação para aceitar apenas numeros.

# Ex: n = leiaint('Digite um n: ')

"""
lista =  list()

def leiaint(msg):
    global n
    n = input(msg)
    for c in range(-10000, 100000):
        lista.append(c)
    while n not in str(lista):
        n = input('\033[1;95mErro!, digite um número inteiro valido: \033[0;0m')
    return n

n = leiaint('Numero: ')
print(f'Você acabou de digitar um número {n}')"""

# Revisão

"""
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro! Digite um número valido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Numero: ')
print(f'Você acabou de digitar um número {n}')"""

### Desafio 105 ### - Correto

# Faça um programa com função notas()
# Que vai ler a nota de varios alunos
# E vai retornar um dicionario
# Com as seguintes informações:

# - Quantidade de notas
# - Maior nota
# - Menor nota
# - Média da turma
# - situação opcional

# Adicionar também as docstrings da função

"""
def notas(* n, sit=False):
    ""
    -> Função para analisar notas e situação de varios alunos
    :param n: Uma ou mais notas dos alunos (aceita varios)
    :param sit: Valor opcional, Indiciando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turmea.
    ""
    boletim = dict()
    lista = list()
    soma = 0

    qtde = len(n)
    boletim['qtde'] = qtde
    maior = max(n)
    boletim['maior'] = maior
    menor = min(n)
    boletim['menor'] = menor
    lista.append(n)
    for c in n:
        soma += c
    med = soma/qtde
    boletim['media'] = med
    if sit == True:
        if med > 7:
            boletim['situação'] = 'Boa'
        elif med > 5 < 7:
            boletim['situação'] = 'Razoavel'
        elif med < 5:
            boletim['situação'] = 'Ruim'
    return boletim


resp2 = notas(3.5, 10, 6.5, sit=True)
resp3 = notas(5.5, 9.5, 10, 6.5, sit=True)
resp1 = notas(3.5, 4.5, 5.5, sit=True)
resp4 = notas(3.5, 4.5, 5.5, sit=False)


print(f'Resultados: ')
print(f'{resp1}')
print(f'{resp2}')
print(f'{resp3}')
print(f'{resp4}')
help(notas)"""

### Desafio 106 ### - Correto

# Faça um mini sistema que utilize o interective help do python
# O usuario vai digitar o comando e o manual vai aparecer
# Quando o usuario digitar a palavra 'FIM'
# O programa encerrar

# OBS: Cores

"""
from time import sleep

def ajuda(msg):
    sleep(1)
    return print(help(msg), flush=True)
while True:
    print('~' * 33)
    print('	\033[1;32mSistema de ajuda em Python\033[0;0m')
    print('~' * 33)
    print('-' * 24)
    comando = str(input('\033[1;93mFunção ou Biblioteca >\033[0;0m'))
    print('-' * 24)
    if comando.upper() == 'FIM':
        break
    ajuda(comando)"""
# print('\033[1;36mAté logo!\033[0;0m')