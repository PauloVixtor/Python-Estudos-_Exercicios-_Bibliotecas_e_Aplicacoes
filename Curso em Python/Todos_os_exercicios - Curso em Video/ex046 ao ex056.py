### Desafio 46 ### - Correto

# Faça programa com contagem regressiva de 0 a 10
# Com pau de 1 segundo entre eles
"""
from time import sleep


for segundos in range(10, 0, -1):
    print('{} Segundos!'.format(segundos))
    sleep(1)
print('Feliz Ano Novo!! "Fogo estourando!" ')"""

### Desafio 47 ### - Correto

# Crie um programa que mostre todos os números pares que estão no intervalo de 0 a 50.
"""
for pares in range(0, 50 + 2, 2):
    print(f'"Contando": {pares}')
"""

## Revisão ##

"""
for pares in range(2, 51 , 2):
    print(f'{pares}', end=' ')
    print('Fim')
"""
### Desafio 48 ### - Corrigido

# Faça um programa que calcule a soma entre os valores impares que são multiplos de 3
# Entre 1 e 500
"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        print(c, end=' ')
        cont += 1
print('\nA soma de todos os valores é {} e a quantida é {}'.format(soma, cont))
"""

### Desafio 49 ### - Correto

# Faça a tabuada
# Usando o valor que o usuario digitar

"""
n = int(input('Digite um número: '))
print('\n** TABUADA **')
print(' ===========')
for tabuada in range(0, 11):
    print(' {} x {} = {}'.format(n, tabuada, n * tabuada))
print(' ===========')
"""

### Desafio 50 ### - Correto

# Crie um programa que leia seis numeros inteiros
# E mostre apenas a soma dos pares. Se for impar desconsiderar.
"""
soma = 0
cont = 0
for contagem in range(0, 6):
    n = int(input('Digite um número: '))
    resto = n % 2
    if resto == 0:
        soma += n
        cont += 1
print(f'A soma dos valores foi {soma} e a quantidade de pares são {cont}!!')
"""


### Desafio 51 ### -

# Crie um programa que leia o priemiro termo á a razão de uma PA
# No final mostre os 10 primeiros termos dessa progressão

"""
n = int(input('Digite o termo : '))
n2 = int(input('Difite a progressão: '))
final = (n + 1) * 20
for contagem in range(n, final + 1, n2):
        print(f'{contagem}', end=' ')"""

## Revisão ##

"""
primeiro = int(input('Digite o termo : '))
razao = int(input('Difite a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('Acabou')"""


### Desafio 52 ### - Correto

# Crie um programa que leia um número inteiro
# Diga se ele é ou não um número primo

"""
n = int(input('Digite um número: '))
for contagem in range(1, n + 1):
    resto = contagem % 2
    if resto == 1:
        if contagem / n == 1 or n == 2:
            print('\nNúmero primo!')
            break
else:
    print('\nNão é um número primo!')
"""

## Revisão ##

"""
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m'
      f'O número {n} foi divisível {tot} vezes!!')
if tot == 2:
    print(f'\nO Número {n} Número primo!')
else:
    print(f'\nO Número {n} não é primo!')"""

### Desafio 53 ### -  Correto

# Crie um programa que leia uma frase
# Diga se ela é palindroma ( consegue se ler ao inverso dela a mesma coisa) Ex: Ana.
# Desconsiderar os espaços
"""
vazio_inverte = ""
frase = str(input('Digite uma frase:')).replace(" ", "").strip().upper()
print(frase)
for palavra in frase.replace(" ", ""):
    vazio_inverte += palavra[::-1]
print(f'O inverso do nome {frase} é {vazio_inverte[::-1]}!')
if frase == vazio_inverte[::-1]:
    print('Essa palavra é Palíndroma!!')
else:
    print('Não palíndroma!!')
"""

## Revisão ##

"""
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
juntos = ''.join(palavra)
inverso = ''
for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]
print(f'O inverso do nome {frase} é {inverso}!')
if frase == inverso:
    print('Essa palavra é Palíndroma!!')
else:
    print('Não palíndroma!!')"""

### Desafio 54 ### -

# Crie um programa que leia o ano de nasciemnto de sete pessoas.
# No final mostre quantas atingiram a maior idade
# E quantas ainda nãoa tingiram

"""
maior_idade = 0
menor_idade = 0

for c in range(0, 7):
    ano = int(input(f'Digite o ano em que a {c + 1}º nasceu: '))
    idade = 2021 - ano
    if idade >= 18:
        maior_idade += 1
    elif idade < 18:
        menor_idade += 1
print(f'De 6 pessoas {maior_idade} tem mais de 18 anos!!')
print(f'De 6 pessoas {menor_idade} tem menos de 18 anos!!')"""

### Desafio 55 ###

# Faça programa que leia o peso de 5 pessoas
# No final mostre qual foi o maior e o menor peso

"""
peso_max = 0
peso_min = 1000000

for c in range(0, 5):
    peso = float(input(f'Digite o seu peso pessoa {c + 1}: '))
    if peso > peso_max:
        peso_max = peso
    elif peso <= peso_min:
        peso_min = peso
print('O maior peso registrado foi {} KG!!'.format(peso_max))
print('O menor peso registrado foi {} KG!!'.format(peso_min))
"""

### Desafio 56 ### - Correto

# Crie um programa que leia nome, idade e sexo de quatro pessoas.
# No final o programa deve mostra:
    # media de idade por grupo
    # Qual nome do homem mais velho
    # quantas mulheres tem menos de 20 anos?
"""
media = 0
qtd = 0

homem_velho = 0
nome_velho = ''

qtd_mulher20 = 0

for c in range(0, 4):
    print(f'=========== Pessoa {c + 1}º ===========')
    nome = str(input(f'Qual seu nome : ')).strip().upper()
    idade = int(input(f'Qual sua idade pessoa : '))
    sexo = str(input(f'Qual seu sexo pessoa [M/F]: ')).upper()
    print('')
    if sexo == 'F' or 'M':
        qtd += 1
        media += idade
    if sexo == 'M':
        if idade > homem_velho:
            homem_velho = idade
            nome_velho = nome
    if sexo == 'F':
        if idade <= 20:
            qtd_mulher20 += 1
print('A média de idade dos grupo foi {:.1f}!!'.format(media/qtd))
print('O homem mais velho tem {} anos e o seu nome é {} !!'.format(homem_velho, nome_velho))
print('Foram {} pessoas do sexo feminino com com menos de 20 anos!!'.format(qtd_mulher20))
"""