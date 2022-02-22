### Desafio 84 ### - Correto

# Faça um programa que leia nome e peso de varias pessoas
# Guarde tudo em uma lista
# Mostre no final
# A) Quantas pessoas foram cadastradas
# B) Um lista com as pessoas mais pesadas
# C) Uma listagem com pessoas mais leves

"""
lista = list()
lista2 = list()
leve = list()
pesado = list()

pessoas = 0

while True:
    lista.append(str(input('Nome:')))
    lista.append(float(input('Peso: ')))
    pessoas += 1
    resp = str(input('Deseja continuar: ')).upper()
    lista2.append(lista[:])
    lista.clear()
    while resp not in 'SsNn':
        resp = str(input('Resposta não encontrada, tente novamente. Deseja continuar: ')).upper()
    if resp in 'Nn':
        break
pesado.append(lista2[0])
leve.append(lista2[0])
for c in lista2:
    if c[1] > pesado[0][1]:
        pesado.clear()
        pesado.append(c)
    if c[1] < leve[0][1]:
        leve.clear()
        leve.append(c)
    if c[1] == pesado[0][1] and c[0] != pesado[0][0]:
        pesado.append(c)
    if c[1] == leve[0][1] and c[0] != leve[0][0]:
        leve.append(c)
print(pesado)
print(leve)


print('-=' * 30)
print(f'As pessoas listadas foram {lista}')
print(f'A) A quantidade de pessoa(s) é {pessoas}!')
print(f'B)O maior peso foi {pesado[0][1]} kg.Peso de ', end='')
for p in pesado:
    print(f'|{p[0]}|', end='')
print(f'\nC)O menor peso foi {leve[0][1]} kg. Peso de ', end='')
for l in leve:
    print(f'|{l[0]}|', end='')"""

### Desafio 85 ### - Correto

# Crie um programa onde o usuario possa digitar sete valores numericos
# E cadastre em uma lista unica
# Que mantenha os numeros pares e impares separados ao final
# Em ordem crescente

"""
numeros = list()
par_impar = [[], []]

for c in range(0, 7):
    numeros.append(int(input(f'Digite o {c + 1}º valor : ')))
    if numeros[c] % 2 == 0:
        par_impar[0].append(numeros[c])
    else:
        par_impar[1].append(numeros[c])
print('-=' * 30)
par_impar[1].sort()
print(f'Os valores impares digitados foram {par_impar[1]}')
par_impar[0].sort()
print(f'Os valores pares digitados foram {par_impar[0]}')"""


### Desafio 86 ### - Correto

# Crie um programa com dimensão 3 por 3 e preencha com valores lidos pelos teclados
# No final mostre a matriz na tela com formatação correta

"""
lista = [[], [], [],
         [], [], [],
         [], [], [],]
for n in range(0, 9):
    lista[n].append(int(input(f'Digite o valor de [0, {n}]:')))
print('-=' * 30)
for c in range(0, 9, 3):
    print(f'{str(lista[c]):^5}', end='')
    print(f'{str(lista[c+1]):^5}', end='')
    print(f'{str(lista[c+2]):^5}')"""

### Desafio 87 ### - Correto

# Aprimorar o desafio anterior mostrando no final
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

"""
lista = [[], [], [],
         [], [], [],
         [], [], [],]

pares = terceira = 0
segundom = [0]
for c in range(0, 9):
    lista[c].append(int(input(f'Digite o valor de [0, {c}]:')))
    if lista[c][0] % 2 == 0:
        pares += lista[c][0]
    if c == 2 or c == 5 or c == 8:
        terceira += lista[c][0]
    if c > 2 and c < 6:
        if lista[c][0] > segundom[0]:
            segundom.clear()
            segundom.append(lista[c][0])
        elif lista[c][0] == segundom[0]:
            segundom.append(lista[c][0])
print('-=' * 30)
print('     MATRIX      ')
for c in range(0, 9, 3):
    print(f'{str(lista[c]):^5}', end='')
    print(f'{str(lista[c + 1]):^5}', end='')
    print(f'{str(lista[c + 2]):^5}')
print(f'\nA) A soma ods valores pares é: {pares}!')
print(f'B) A soma dos valores da terceira coluna é {terceira}!')
print(f'C) O maior valor da segunda linha é  {segundom[0]}!')
# print('-=' * 30)"""

### Desafio 88 ### - Correto

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# O programa vai perguntar quantos jogos serão criados
# Vai sortear 6 numeros de 1 a 60
# Tudo em uma lista composta

"""
import random
from time import sleep

lista = []
listaf = []

print('=' * 25)
print('   JOGAR NA MEGA SENA')
print('=' * 25)
qtd = int(input('Quantos jogos você quer sortear: '))
print('-=' * 3, f'SORTEANDO {qtd} JOGOS', '-=' * 3)
for c in range(0, qtd):
    for n in range(0, 6):
        lista.append(random.randint(1, 60))
    listaf.append(lista[:])
    lista.clear()
    sleep(2)
    print(f'Jogo {c + 1}: {sorted(listaf[c])}')"""

### Desafio 89 ### - Correto

# Crie um programa que leia nome e duas notas de um aluno
# Guarde tudo em uma lista composta
# No final mostre o boletim contendo media de cada um
# Permitindo que o usuario possa mostrar as notas individuais de cada aluno

"""
alunos = []
temp = []
cont = 0
while True:
    temp.append(str(input('Nome do aluno:')).title().strip())
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))
    cont += 1
    alunos.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar [S/N]: ')).upper()
    while resp not in 'sSnN':
        resp = str(input('Não encontrada resposta, tente novamente. Deseja continuar [S/N]: ')).upper()
    if resp in 'Nn':
        break
print('-=' * 30)
print('Nº|   ', 'Nome   ', '| Média   ')
print('-' * 60)
for c in range(0, cont):
    print(f'{str(c):^8}', end='')
    print(f'{str(alunos[c][0]):^8}', end='')
    med = (alunos[c][1] + alunos[c][2]) / 2
    print(f'{str(med):^2}')
print('-' * 60)
aluno = int(input('Mostrar nota de qual aluno (999 interrompe o programa): '))
while aluno != 999:
    print(f'Notas de {str(alunos[aluno][0]):^2} são {str(alunos[aluno][1:3]):^2}')
    print('-' * 60)
    aluno = int(input('Mostrar nota de qual aluno (999 interrompe o programa): '))"""
