### Desafio 57 ### - Correto

# Faça um programa que leia o sexo de uma pessoa ( M ou F)
# Se digitar errado, peça para ele refazer.

"""
sexo = False
sexo_esc = ''
while sexo == False:
    sexo_esc = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0] # pega ultima letra digitada.
    if sexo_esc == 'M' or sexo_esc == 'F':
        sexo = True
    else:
        print('Não encontrado, digite novamente!')
if sexo_esc == 'M':
    print('\nSeu sexo é Masculino!')
if sexo_esc == 'F':
    print('\nSeu sexo é Feminino!')"""

## Verificação ##

"""
sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, Informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com Sucesso.')"""

### Desafio 58 ### - Correto

# Melhore o desafio 28
# Onde computador vai pensar em um numero de 0 a 10.
# O jogo deve tentar ate acertar
# Depois deve ser mostrado quantas vezes foram tentadas.

"""
import random


lista = []
for n in range(0, 10 + 1):
    lista += [n]
computador = random.choice(lista)
tentativas = 0
game = False
while game == False:
    jogador = int(input('Digite um número de 0 a 10: '))
    if jogador == computador:
        print('===============')
        print(' Você Acertou!')
        print(' Venceu o Game!')
        print('===============')
        tentativas += 1
        game = True
    else:
        print('===============')
        print('  Você Errou!    ')
        print('Tente novamente!')
        print('===============')
        deseja = str(input('Deseja continuar? [S/N]: ')).upper()
        tentativas += 1
        if deseja == 'N':
            print('===============')
            print('  Game Over!   ')
            print('===============')
            game = True
print(f'Você fez {tentativas} tentativas!')"""

### Desafio 59 ### - Correto

# Crie um programa que leia dois valores
# Mostre um menu com SOMA, MULTIPLICAÇÃO, MAIOR, NOVOS NUMEROS e SAIR DO PROGRAMA

"""
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

lista = [1, 2, 3, 4, 5]
programa = True
while programa == True:
    print('=================================')
    print('     Seja Bem Vindo!             ')
    print('     [1] SOMA                    ')
    print('     [2] MULTIPLICAÇÃO           ')
    print('     [3] MAIOR                   ')
    print('     [4] NOVOS NUEMROS           ')
    print('     [5] SAIR                    ')
    print('=================================')
    opcao = int(input('Escolha uma opcao:   '))
    if opcao == lista[0]:
        soma = numero1 + numero2
        print(f'\n O soma de {numero1} + {numero2} = {soma}!')
    elif opcao == lista[1]:
        mult = numero1 * numero2
        print(f'\n A multiplicação de {numero1} * {numero2} = {mult}!')
    elif opcao == lista[2]:
        if numero1 > numero2:
            print(f'\n O número {numero1} é maior que {numero2}, ou seja, o primeiro é maior que o segundo!')
        elif numero2 > numero1:
            print(f'\n O número {numero2} é maior que {numero1}, ou seja, o segundo é maior que o primeiro!!')
        else:
            print(f'Primeiro e segundo números são iguais!')
    elif opcao == lista[3]:
        print('Informe os valores novamente!')
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite um número: '))
    elif opcao == lista[4]:
        print('Saindo....')
        programa = False
    else:
        print('Resposta não encontrada digite novamente')
print('FIM DO PROGRAMA')"""

### Desafio 60 ### - Correto

# Faça programa que leia um número e faça seu fatorial

"""
n1 = int(input('Digite um número: '))
resultado = n1
while n1 != 1:
    if n1 == 5:
        print(f'{n1} x ', end='')
    n1 -= 1
    resultado = resultado * n1
    n_t = n1
    print(f'{n_t} ', end='')
    if n_t != 1:
        print(' x ', end='')
print(f'= {resultado}')
print('FIM!')"""

## Revisão ##

# Usando biblioteca

"""
from math import factorial

n = int(input('Digite um número para calcular seu factorial: '))
f = factorial(n)
print('factorial de {} é {}'.format(n, f))"""

### Desafio 61 ### - Correto

# Refaça o desafio 51, lendo primeiro termo e a razão
# Mostrando os 10 primeiros termos
# Usano while

"""
primeiro = int(input('Digite o termo : '))
razao = int(input('Digite a Razão: '))
print(f'{primeiro}', end=' → ')
resultado_final = primeiro + (10 - 1) * razao
decimo = primeiro
while resultado_final != decimo:
    decimo = decimo + razao
    print('{}'.format(decimo), end=' → ')
print('Acabou!')"""

### Desafio 62 ### - Correção

# Melhore desafio 61, perguntando se ele quer fazer mais algum termo

"""
termo = True
while termo == True:
    primeiro = int(input('Digite o termo : '))
    razao = int(input('Digite a Razão: '))
    print(f'{primeiro}', end=' → ')
    resultado_final = primeiro + (10 - 1) * razao
    decimo = primeiro
    while resultado_final != decimo:
        decimo = decimo + razao
        print('{}'.format(decimo), end=' → ')
    if resultado_final == decimo:
        print('Acabou!')
    deseja = str(input('Deseja fazer mais algum termo [S/N]: ')).upper()
    if deseja == 'S':
        termo = True
    if deseja == 'N':
        termo = False
        print('Fim!')"""

## Revisão ##

"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o termo : '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mais: '))
print('\nFIM!\n')
print('Progressão finalizada com sucesso! {}'.format(total))"""

### Desafio 63 ### - Correto

# Leia um numero
# Mostre na tela a sequencia de fibonacce

"""
n1 = int(input('Digite um número: ')) - 2
fib = 1
fib_prox = 0
resultado = 0
print('{}'.format(fib_prox), end=' → ')
print('{}'.format(fib), end=' → ')
while n1 != 0:
    resultado = fib + fib_prox
    fib_prox = fib
    fib = resultado
    print('{}'.format(resultado), end=' → ')
    n1 -= 1
print('FIM!')"""

### Desafio 64 ### -

# Crie um programa que leia varios numeros inteiros
# O criterio de parada é 999.
# Mostre a quantidade e a soma

"""
qtd = 0
soma = 0
n1 = 0

while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]: '))
    if n1 != 999:
        qtd += 1
        soma += n1
print(f'A quantidade de tentativas foi {qtd}!')
print(f'A soma dos números foi {soma}!')"""

### Desafio 65 ### - Correto (com bug devido mudança)

# Crie um programa que leia varios numeros
# no final mostre a media entre todos
# E o menor e maior valor lido
# o programa deve perguntar se o usuario quer ou não continuar

"""
n1 = 0
qtd = 0
soma = 0

maior = 0
menor = 100000000000000

deseja = ''
continuar = True
while continuar == True :
    n1 = int(input('Digite um numero: '))
    qtd += 1
    soma += n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    deseja = str(input('Deseja continuar [S/N]: ')).upper()
    while deseja not in 'SN':
        print('Não enontrado!')
        deseja = str(input('Deseja continuar [S/N]: ')).upper()
    if deseja == 'S':
        n1 = int(input('Digite um numero: '))
        deseja = str(input('Deseja continuar [S/N]: ')).upper()
        if deseja in 'S':
            continuar = False
            print('\nA média foi de {:.2f}!'.format(soma / qtd))
            print(f'O Menor número digitado é o {menor}')

    # print(f'O Maior número digitado é o {maior}')"""


# Dica faça o programa em partes
"""
resp = 'S'
soma = quant = media = maior = menor = 0 # todas variaveis recebem 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print('Você digitou {}, a soma foi {} é a média foi {:.1f}!'.format(quant, soma, media))"""
# print(f'Menor número foi {menor} e o maior foi {maior}!')