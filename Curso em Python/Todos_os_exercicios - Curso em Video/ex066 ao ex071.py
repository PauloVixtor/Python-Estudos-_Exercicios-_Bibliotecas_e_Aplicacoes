### Desafio 66 ### - Correto

# Crie um programa que leia varios numeros até numero 999
# No final some os numeros e mostre na tela, sem o criterio de parada.
"""
s = 0
cont = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor != 999:
        s += valor
        cont += 1
    else:
        break
print(f'A soma dos {cont} valores foi {s}!!')
"""

### Desafio 67 ### - Correto

# Faça um programa que faça a tabuada de varios numeros
# Um de cada vez
# Para cada Valor do usuario
# O programa interrompe se o valor for negativo

"""
while True:
    numero = int(input('Quer ver a tabuada de qual valor: '))
    if numero >= 0:
        print('------------------')
        for c in range(1, 11, 1):
            vezes = c * numero
            print(f'{numero} x {c} = {vezes}')
        print('------------------')
    else:
        break
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
"""

### Desafio 68 ### - Correto

# Faça um programa que jogue par ou impar com computador.
# Jogo só será interrompido se o jogador perder.
# Mostrar total de vitorias consecutivas que ele conquistou no final do jogo.

"""
import random

cont = 0
while True:
    computador = random.randint(1, 10)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
    jogador = int(input('Digite um valor: '))
    p = str(input('Par ou impar [P/I]: ')).strip().upper()
    while p not in 'IP':
        print('OPção invalida, digite novamente!')
        p = str(input('Par ou impar [P/I]: ')).strip().upper()
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'\nVocê jogou {jogador} e o computador {computador}. Total é {soma}, deu PAR ')
        if p == 'P':
            print('\nVocê Venceu!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('\nVocê Perdeu!')
            print('Tente novamente mais tarde!')
            break
    if soma % 2 == 1:
        print(f'\nVocê jogou {jogador} e o computador {computador}. Total é {soma}, deu IMPAR ')
        if p == 'I':
            print('\nVocê Venceu!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('\n Perdeu!')
            print('Tente novamente mais tarde!')
            break
print(f'GAME OVER! Você venceu {cont} vezes.')
"""

### Desafio 69 ### - Correto

# Crie um programa que leia a idade e sexo de varias pessoas
# A cada pessoa cadastrada, o programa deve perguntar se tem mais algum cadastro

# A) Quantas pessoas tem mais de 18 anos?
# B) Quantos homens foram cadastrados?
# C) Quantas mulheres tem menos de 20 anos?

"""
a = 0
b = 0
c = 0
while True:
    print('------------------------')
    print('  CADASTRE UMA PESSOA   ')
    print('------------------------')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        print('Não Valido, digite novamente!')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        a += 1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade >= 20:
        c += 1
    deseja = str(input('Deseja continuar cadatrando [S/N]:')).strip().upper()
    while deseja not in 'SN':
        print('Não Valido, digite novamente!')
        deseja = str(input('Deseja continuar cadatrando [S/N]:')).strip().upper()
    if deseja == 'N':
        break
    if deseja == 'S':
        continue
print('=======FIM DO PROGRAMA======')
print(f'\nForam {a} pessoas com mais de 18 anos!')
print(f'Foram {b} homens cadastrados!')
print(f'Foram {c} mulheres com mais de 20 anos!')

"""

### Desafio 70 ### - Correto

# Crie um programa que leia o nome e o preço de varios produtos
# Perguntar ao final se deseja continuar?

# A) Qual o total de gasto da compra?
# B) Quantos produtos custam mais de R$1.000,00
# C) Qual é o nome do produto mais barato?

"""
a = 0
b = 0
c = 1000
c_p = ''

print('------------------------')
print('   LOJA SUPER BARATÃO   ')
print('------------------------')
while True:
    nome_p = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: '))

    a += preco
    if preco >= 1000:
        b += 1
    if preco < c:
        c = preco
        c_p = nome_p

    deseja = str(input('Deseja continuar cadatrando [S/N]:')).strip().upper()
    while deseja not in 'SN':
        print('Não Valido, digite novamente!')
        deseja = str(input('Deseja continuar cadatrando [S/N]:')).strip().upper()
    if deseja == 'N':
        break
    if deseja == 'S':
        continue
print('O total da compra foi R${:.2f}'.format(a))
print(f'Temos {b}  produtos que custam mais de R$ 1.000,00 !')
print('O produto mais barato foi {} que custa R${:.2f}'.format(c_p, c))"""

### Desafio 71 ### - Correto

# Crie um programa que simula um CAIXA ELETRONICO
# No inicio informe o valor a ser sacado
# Programa informa quantas cedulas de cada valor serão entregues

# Considere as notas de R$50, R$20, R$10 e R$1

"""
saldo = 10000
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
sacar_valor = 0

print('------------------------')
print('     BANCO DO PAULO     ')
print('------------------------')
while True:
    print('---------------------------')
    print('Seu saldo atual é R$ {:.2f}'.format(saldo))
    print('---------------------------')
    sacar = int(input('Que valor você quer sacar? R$'))
    saldo -= sacar
    sacar_valor = sacar
    while saldo < sacar:
        print('Saldo insuficiente, digite um valor valido')
        sacar = int(input('Que valor você quer sacar? R$'))
    while sacar > 50:
        sacar -= 50
        cont_50 += 1
    while sacar > 20:
        sacar-= 20
        cont_20 += 1
    while sacar > 10:
        sacar -= 10
        cont_10 += 1
    while sacar > 1:
        sacar -= 1
        cont_1 += 1
    deseja = str(input('Deseja continuar [S/N]:')).strip().upper()
    while deseja not in 'SN':
        print('Não Valido, digite novamente!')
        deseja = str(input('Deseja continuar [S/N]:')).strip().upper()
    if deseja == 'N':
        break
    if deseja == 'S':
        continue

print(f'Total de {cont_50} cedulas de R$50,00')
print(f'Total de {cont_20} cedulas de R$20,00')
print(f'Total de {cont_10} cedulas de R$10,00')
print(f'Total de {cont_1} cedulas de R$1,00')
print('Saldo atual: R${:.2f}'.format(saldo))
"""
