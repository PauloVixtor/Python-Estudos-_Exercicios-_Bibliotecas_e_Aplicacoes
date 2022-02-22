### Desafio 78 ### - Correto

# Faça um programa que leia 5 valores numericos e guarde em uma lista
# No final mostre qual foi o maior e o menor valor digitado
# E suas posições na lista

"""
todos = []
maxi = []
mini = []


for c in range(0, 5):
    numero = int(input(f'Digite o número na posição {c}: '))
    todos.append(numero)
maximo = max(todos)
minimo = min(todos)
for cont in range(0, len(todos)):
    if maximo == todos[cont]:
        maxi.append(cont)
    if minimo == todos[cont]:
        mini.append(cont)
print('---------------------------------')
print(f'Você digitou os valores {todos}')
print(f'O Maior valor foi  {maximo} na posições ', end='')
for v in range(0, len(maxi)):
    print(f'{maxi[v]}...', end='')
print(f'\nO Menor valor foi  {minimo} na posições ', end='')
for y in range(0, len(mini)):
    print(f'{mini[y]}...', end='')"""


#### Revisão ####

todos = []
maxi = []
mini = []

"""
for c in range(0, 5):
    todos.append(int(input(f'Digite o número na posição {c}: '))) # Forma como adicionar a lista!!!
maximo = max(todos)
minimo = min(todos)
for cont in range(0, len(todos)):
    if maximo == todos[cont]:
        maxi.append(cont)
    if minimo == todos[cont]:
        mini.append(cont)
print('---------------------------------')
print(f'Você digitou os valores {todos}')
print(f'O Maior valor foi  {maximo} na posições ', end='')
for v in range(0, len(maxi)):
    print(f'{maxi[v]}...', end='')
print(f'\nO Menor valor foi  {minimo} na posições ', end='')
for y in range(0, len(mini)):
    print(f'{mini[y]}...', end='')"""

### Desafio 79 ### - Correto

# Crie um programa que o usuario pode digitar diversos valores numericos
# E adicione em uma lista
# Caso o numero já exista ele não será adicionado
# serão mostrado todos os valores em ordem crescente

"""
lista = []
numero = int(input('Digite um número: '))
lista.append(numero)
print('Valor adicionado com sucesso!')
p = str(input('Deseja continuar: [S/N]'))
while (p).upper() not in 'SN':
    p = str(input('Opção não encontrada digite novamente. Deseja continuar: [S/N]'))
while (p).upper() != 'N':
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado não será adicionado!')
    p = str(input('Deseja continuar: [S/N]'))
    while (p).upper() not in 'SN':
        p = str(input('Opção não encontrada digite novamente. Deseja continuar: [S/N]'))
print(f' Você digitou os valores: {sorted(lista)}')"""


### Desafio 80 ### - Revisão

# Crie um programa que o usuario pode digitar 5 valores numericos
# Cadastre na lista, já na posição correta( sem o orted)
# No final mostre ordenada


"""
n = int(input('Digite um número: '))
lista = []
lista.append(n)
print('Adiconado ao final da lista')

for c in range(0, 4):
    n = int(input('Digite um número: '))
    if n >= max(lista):
        lista.append(n)
        print('Adiconado na posição ', end='')
        for cont in range(0, len(lista)):
            if lista[cont] == n:
                print(f'{cont}')
    elif n <= min(lista):
        lista.insert(0, n)
        print('\nAdiconado na posição ', end='')
        for cont2 in range(0, len(lista)):
            if lista[cont2] == n:
                print(f'{cont2}')
print(f'\nOs valores em ordem são: {lista}')"""

#### Revisão ####

"""
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]: # Se o numero for o primeiro a ser digitado ou maior que o digitado e adiconado ao final
        lista.append(n)
        print('Adiconado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado a posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')"""


### Desafio 81 ### - Correto

# Crie um programa que leia varios numeros
# E coloque todos em uma lista
# A) Quantos elementos tem na lista
# B) Ordem descrecente
# Se o valor 5 for digitado ou não na lista

"""
lista = []
numero = int(input('Digite um número: '))
lista.append(numero)
print('Valor adicionado com sucesso!')
p = str(input('Deseja continuar: [S/N]'))
while (p).upper() not in 'SN':
    p = str(input('Opção não encontrada digite novamente. Deseja continuar: [S/N]'))
while (p).upper() != 'N':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    print('Valor adicionado com sucesso!')
    p = str(input('Deseja continuar: [S/N]'))
    while (p).upper() not in 'SN':
        p = str(input('Opção não encontrada digite novamente. Deseja continuar: [S/N]'))

print(f'A) Você digitou {len(lista)} elementos')

lista.sort(reverse=True)
print(f'B) O total de número digitados foi: {lista}')

x = 0
for c in range(0, len(lista)):
    if lista[c] == 5:
        x += 1
print(f'C) A quantidade de vezes que 5 foi digitado {x} vez!')"""


### Desafio 82 ### - Correto

# Crie um programa que vai ler varios numeros
# E colocar em uma lista
# Depois crie duas listas uma para numeros pares eoutra para impares
# Ao final mostre o conteudo das três listas geradas

"""
lista = []
lista_par = []
lista_impar = []

numero = int(input('Digite um número: '))
lista.append(numero)
print('Valor adicionado com sucesso!')
if numero % 2 == 0:
    lista_par.insert(0, numero)
    print('Valor adicionado com sucesso na lista PAR!')
else:
    lista_impar.insert(0, numero)
    print('Valor adicionado com sucesso na lista IMPAR!')
p = str(input('Deseja continuar [S/N]: '))
while (p).upper() not in 'SN':
    p = str(input('Opção não encontrada digite novamente. Deseja continuar: [S/N]'))
while (p).upper() != 'N':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    print('Valor adicionado com sucesso!')
    if numero % 2 == 0:
        lista_par.append(numero)
        print('Valor adicionado com sucesso na lista PAR!')
    else:
        lista_impar.append(numero)
        print('Valor adicionado com sucesso na lista IMPAR!')
    p = str(input('Deseja continuar [S/N]: '))
print('=================================================')
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')"""

### Desafio 83 ### - Correto

# Crie um programa onde usuario digite uma expressão
# (Qualquer coisa que usa parentes)
# Seu programa deve analisar se a expressão passada está com parentes aberto e fechado na ordem certa

"""
lista = []
cont1 = 0

exp = str(input('Digite uma expressão: '))
for adc in range(0, len(exp)):
    lista.append(exp[adc])
# print(exp[1])
for c in range(0, len(lista)):
    if '(' in lista[c]:
        cont1 += 1
    if ')' in lista[c]:
        cont1 += 1
if cont1 % 2 == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')"""


