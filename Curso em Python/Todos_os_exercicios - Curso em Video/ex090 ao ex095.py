### Desafio 90 ### - Correto

# Faça um programa que leia o nome e media de um aluno
# Guardando também a situação em um dicionario
# No final mostre o conteudo da estrutura na tela

"""
aluno = dict()

nome = str(input('Nome: ')).strip().title()
aluno['nome'] = nome
media = float(input(f'Média de {nome}: '))
aluno['media'] = media
if media > 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'A situção do aluno é {aluno["situacao"]}')
"""

### Desafio 91 ### - Correto

# Crie um programa onde 4 jogadores joguem um dado
# E tenh resultados aleatorios
# Guarde esse resultados em um dicionario
# No final coloque o dicionario em ordem
# Sabendo que o vencedor tirou o maior numero

"""
import random
from time import sleep
jogadores = {}

print('Valores Sorteados:')
for c in range(0, 4):
    numero = random.randint(1, 6)
    jogadores[f'Jogador {c + 1}'] = numero
    sleep(1)
    print(f'    O jogador {c + 1} tirou {numero}')
print('==Ranking de jogadores:')
vencedor = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
for e in range(0, 4):
    sleep(1)
    print(f'{e + 1}º lugar: {vencedor[e][0]} com {vencedor[e][1]}')
"""

### Desafio 92 ### - Correto

# Crie um programa que leia nome, ano de nascimento, carteira de trabalho e cadastre-os.( adicione a idade) Em dicionario.
# Se Caso a carteira de trabalho for igual a 0 o dicionario vai receber tambem o ano de contratação e salario
# Além de calcaular a idade que a pessoa vai se aposentar.( Se aposenta depois de 35 anos de contribuição)

"""
pessoa = dict()

nome = str(input('Digite seu nome: ')).title().strip()
pessoa['nome'] = nome
nasc = int(input('Digite o ano de seu nascimento: '))
idade = 2022 - nasc
pessoa['idade'] = idade
carteira = int(input('Digite a sua carteira de trabalho: '))
pessoa['carteira'] = carteira
if carteira != 0:
    contratacao = int(input('Digite o ano de contração: '))
    pessoa['contratacao'] = contratacao
    salario = float(input('Digite o valor do seu salario R$: '))
    pessoa['salario'] = salario
    pessoa['aposentadoria'] = int(contratacao) + 35 - 2022


print('=-=' * 20)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}!')
"""


### Desafio 93 ### - Correto

# Crie um programa que gerencie o aproveitamento de um jogador de futebol
# Programa vai ler> NOME DO JOGADOR, QTDE DE PARTIDAS JOGADAS
# Depois ler a quantidade de gols feitos em cada partida
# No final tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

"""
campeonato = {}
lista_gol = []
total = 0

jogador = str(input('Nome do jogador: ')).strip().title()
campeonato['jogador'] = jogador
partidas = int(input(f'Quantas partidas {jogador} jogou: '))

for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}: '))
    lista_gol.append(gols)
    total += gols
campeonato['gols'] = lista_gol
campeonato['total'] = total
print('=-=' * 20)
print(campeonato)
print('=-=' * 20)
for k, v in campeonato.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-=' * 20)
print(f'O jogador {jogador} jogou {partidas}.')
for e in range(0, partidas):
    print(f'    => Na partida {e}, fez {lista_gol[e]} gols.')
print(f'Foi um total de {total} gols.')"""

### Desafio 94 ### - Correto

# Crie um programa que leia NOME, SEXO e IDADE de varias pessoas.
# Guarde os dados de cada pessoa em um dicionario
# E todos os dicionarios em uma lista.
# Mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas pessoas com idade acima da média

"""
lista_pessoas = []

while True:
    pessoas = {}
    nome = str(input('Nome: ')).strip().title()
    pessoas['nome'] = nome
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Resposta não encontrada. Digite novamente Sexo: [M/F] ')).upper().strip()
    pessoas['sexo'] = sexo
    idade = int(input('Idade: '))
    pessoas['idade'] = idade
    lista_pessoas.append(pessoas.copy())
    del pessoas
    continuar = str(input('Deseja continuar: [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Resposta não encontrada. Deseja continuar: [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(lista_pessoas)
print('=-=' * 20)

print(f'A) o grupo tem {len(lista_pessoas)} pessoas cadastradas!')

soma_idade = 0
lista_mulheres = []
armaz = ''
for c in lista_pessoas:
    for k, v in c.items():
        if k == 'nome':
            armaz = v
        if k == 'idade':
            soma_idade += v
        if k == 'sexo':
            if v == 'F':
                lista_mulheres.append(armaz)
media = soma_idade / len(lista_pessoas)
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for cont in lista_mulheres:
    print(cont, end=' ')
print(f'\nD) Lista de pessoas que estão a cima da média: \n')
acima_media = []
cont = 0
for e in lista_pessoas:
    for col, val in e.items():
        if col == 'idade':
            if val > media:
                acima_media.append(lista_pessoas[cont])
    cont += 1
for vezes in acima_media:
    for coluna, valor in vezes.items():
        print(f'{coluna} = {valor};', end=' ')
    print('\n')
print('<<ENCERRADO>>')"""


### Desafio 95 ### - Correto

# Aprimore o desafio 093 para que funcione  com varios jogadores
# Incluindo um sistema de visualização de aproveitamento de cada jogador

"""
lista_jogadores = []
while True:
    total = 0
    campeonato = {}
    lista_gol = []
    print('=-=' * 30)
    jogador = str(input('Nome do jogador: ')).strip().title()
    campeonato['jogador'] = jogador
    partidas = int(input(f'Quantas partidas {jogador} jogou: '))

    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c}: '))
        lista_gol.append(gols)
        campeonato['gols'] = lista_gol
        total += gols
    campeonato['total'] = total
    lista_jogadores.append(campeonato.copy())
    del campeonato
    deseja = str(input('Deseja continuar: [S/N]')).upper().strip()
    while deseja not in 'SN':
        deseja = str(input('Rsposta não encontrada. Deseja continuar: [S/N]')).upper().strip()
    if deseja == 'N':
        break
print('=-=' * 30)
print(lista_jogadores)
print('=-=' * 30)
print(f'COD         NOME              GOLS                    TOTAL')
print('-' * 30)
cont = 0
for c in lista_jogadores:
    print(f'\n{cont}', end=' ')
    for v in c.values():
        print(f'{str(v):>14}', end=' ') # :<10 = espaços a esquerda // :>10 = espaços a direita // :^10 = centralizado.
    cont += 1
print('\n')
mostrar = int(input('Deseja mostrar qual dos jogador: '))
while mostrar > len(lista_jogadores):
    print(f'Erro não existe jogador com numero {mostrar}!. Tente novamente.')
    mostrar = int(input('Deseja mostrar qual dos jogador(Digite 999 para PARAR!): '))
while mostrar != 999:
    print('-' * 30)
    for k, v in lista_jogadores[mostrar].items():
        if k == 'jogador':
            print(F'--LEVANTAMENTO DO JOGADOR {v}')
        if k == 'gols':
            for gol in range(0, len(v)):
                print(f'    => Na partida {gol}, fez {v[gol]} gols.')

    mostrar = int(input('Deseja mostrar qual dos jogador: '))
    if mostrar == 999:
        break
    while mostrar > len(lista_jogadores):
        print(f'Erro não existe jogador com numero {mostrar}!. Tente novamente.')
        mostrar = int(input('Deseja mostrar qual dos jogador: '))
        if mostrar == 999:
            break
"""
