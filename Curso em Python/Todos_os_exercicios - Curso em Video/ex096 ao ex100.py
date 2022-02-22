### Desafio 96 ### - Correto

# Faça um programa que tenha uma função chamada area(), que recebe as dimensões
# De um terreno retangular ( largura e comprimento)
# Mostra area e terreno

"""
def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area_terreno} m²')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)"""

### Desafio 97 ### - Correto

# Faça um programa que tenha a função escreva()
# Que recebe um texto qualquer como parametro
# E mostra uma mensagem com tamanho adaptavel

"""
def escreva(mensagem):
    cont_letra = len(mensagem) + 4
    print('~' * cont_letra)
    print(f'  {mensagem}  ')
    print('~' * cont_letra)

escreva('Paulo Victor')
escreva('Curso de python no you tube')
escreva('CEV')
"""

### Desafio 98 ### - Correto // estudar novamente o video!

# Faça um programa que tenha uma função chamado contador(), que recebe 3 parametros
# Parametros: Inicio, Fim e Passo. E Realiza a contagem
# Seu programa tem que realizar 3 contagens atraves da função criada.
# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada

"""
from time import sleep

def contador(inicio, fim, passo):
    print('=-' * 30)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    if passo == 0:
        passo += 1
    if inicio < fim:
        fim += 1
        for c in range(inicio, fim, passo):
            print(f'{c}', end=' ')
            sleep(0.4)
        print('FIM!')
    if inicio > fim and passo > 0:
            fim -= 1
            for c in range(inicio, fim, - passo):
                print(f'{c}', end=' ')
                sleep(0.4)
            print('FIM!')
    if inicio > fim and passo < 0:
            fim -= 1
            for c in range(inicio, fim, passo):
                print(f'{c}', end=' ')
                sleep(0.4)
            print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
comeca = int(input(f'Inicia: '))
termina = int(input(f'Fim: '))
proximo = int(input(f'Passo: '))
contador(comeca, termina, proximo)"""


### Desafio 99 ### - Correto

# Faça um programa que tenha a função maior()
# Que recebe varios parametros com valores inteiros
# O programa terá que analisar os numeros e dizer qual é o maior.

# Primeira forma de fazer
from time import sleep
"""
def maior(* num):
    maximo = max(num)
    cont = len(num)
    print('=-' * 30)
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {cont} valores ao todo!', flush=True)
    sleep(0.4)
    print(f'O maior número informado é o {maximo}')

maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1, 2)
maior(6)
maior(0)"""

"""
from time import sleep


def maior(* num):
    lista = list(num)
    maximo = max(num)
    cont = len(num)
    soma = 0
    for e in num:
        soma += e
    print('=-' * 30)
    print('Analisando os valores passados...')
    if soma > 1:
        for c in lista:
            print(f'{c}', end=' ', flush=True)
            sleep(0.4)
    if soma < 1:
        cont -= 1
        print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior número informado é o {maximo}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)"""

### Desafio 100 ### -

# Faça um programa que tenha uma lista chamada numeros
# Faça duas funções chamadas Sorteio e SomaPar()
# A primeira vai sortear 5 numeros e coloca-los dentro de uma lista
# A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

"""
import random
from time import sleep

numeros = list()
def sorteio():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = random.randint(0, 10)
        sleep(0.4)
        print(f'{num}', end=' ', flush=True)
        numeros.append(num)
    print('PRONTO!')
def somapar():
    sleep(0.4)
    print(f'Somando os valores pares de {numeros} ', end='')
    soma = 0
    for e in numeros:
        if e % 2 == 0:
            soma += e
    print(f'temos {soma}')

sorteio()"""
# somapar()
