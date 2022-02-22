### Desafio 28 ### - Correto

# 28 - Faça o computador pensar em um numero de 1 a 5, e depois peça para o usuario tentar adivinhar
# Caso ele acerte mostre uma mensgaem, se ele errar mostre outro.

"""
import random

 lista = [0, 1, 2, 3, 4, 5]
 esc = random.choice(lista)
 num1 = int(input('Digite de um 1 a 5: '))
 while num1 > 5:
   num1 = int(input('Digite de um 1 a 5: '))
   break
 print('O número pensado pela maquina é {}!!'.format(esc))
 if num1 == esc:
    print('Você acertou o número Parabéns, o número é {} e você escolheu {}!!'.format(esc, num1))
 else:
    print('Você errou tente de novo, o número é {} e você escolheu {}!!'.format(esc, num1))
"""

## Correção 28 ##

"""
from random import randint
from time import sleep

computador = randint(1, 5) # Faz o computador sortear um número
print('=' * 30)
print('Tente avinhar o número escolhido....')
print('=' * 30)
jogador = int(input('Escolha um número de 1 a 5: ')) # Jogador tentar advinhar
print('PROCESSANDO.....')
sleep(3)
if jogador == computador:
    print('Parabéns, Você consegiu me vencer!!')
else:
    print(f'Ganhei, Eu pensei em {computador} e não em {jogador}')
"""
### Desafio 29 ### - correto

# 29 - Escreva um programa que leia a velocidade de um carro

# Se ela for maior que 80 km, mostra uma mwnsgaem que o carro tomou uma multa
# A cada um KM ultrapassado é R$ 7,00 a mais

"""
vel = int(input('Qual a velocidade atual do carro?: '))
print('A velocidade do seu Carro está à {} KM/H!!'.format(vel))
multa = vel - 80 # calculando a multa
if vel > 80:
   print('=' * 30)
   print('Você passou do limite de 80 KM, é recebeu uma multa!!')
   valor = multa * 7
   print('O Valor que deve ser pago é {:.2f}, tenha mais cudiado!!'.format(valor))
   print('=' * 30)
else:
   print('=' * 30)
   print('Você está entre o limite, continue assim!!')
   print('=' * 30)
"""



### Desafio 30 ### - Correto

# Crie um programa que leia um número inteiro e diga se ele e par ou impar

"""
numero1 = int(input('Digite um número qualquer?: '))
resto = numero1 % 2 # O resto de qualquer divisão par por %2 é 0, e o resto de impar dividido por %2 e 1

if resto == 0:
   print('O número {} é par!!'.format(numero1))
else:
   print('O número {} é impar!!'.format(numero1))
"""

### Desafio 31 ###

# Desenvolva um programa que leia uma Viagem
# Calcule o preço da viagem cobrando 0,50 centavos até 200 km
# Acima disso o preço cobrado e 0,45.

'''
km = int(input('Digite a quantidade de Quilometros da sua viagem: '))
if km >= 200:
   valor50 = km * 0.45
   print('A sua viagem é de {} Km, e o valor é R$ {:.2f}'.format(km, valor50))
else:
   valor45 = km * 0.50
   print('A sua viagem é de {} Km, e o valor é R$ {:.2f}'.format(km, valor45))
'''
## Simplificado ##

"""
distancia = float(input('Digite a quantidade de quilometros da sua viagem: '))
print(f'Você vai fazer uma viagem de {distancia} km') # Mostra a distancia digitada...
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # simplifica o if é o else na linha da questão
print('É o preço da sua passagem é R${:.2f}'.format(preço))
"""

### Desafio 32 ### -  Correto

# Faça um programa que leia um ano
# Mostre se ele e bissexto

"""
from datetime import date

inf_ano = int(input('Qual ano você quer saber se é bissexto?(Se digitar 0, ele puxa o ano atual):  '))
if inf_ano == 0:
    inf_ano = date.today().year # Puxa o ano atual no lugar de 0
if inf_ano % 4 == 0 and inf_ano % 100 !=0 or inf_ano % 400 ==0: # Se o número e divido por 4, diferente de 100 com execessão de 400 , ele e bissexto
    print(f'O ano {inf_ano} é bissexto!!')
else:
    print(f'O ano {inf_ano} não é bissexto')
"""

### Desafio 33 ### - Correto

# Faça um programa que leia 3 numeros
# E mostre qual é o maior é qual e o menor
"""
number1 = int(input('Digite um número inteiro: ')) # 1
number2 = int(input('Digite um número inteiro: ')) # 2
number3 = int(input('Digite um número inteiro: ')) # 3

lista = [number1, number2, number3]
maior = max(lista)
print(f'O maior número é o {maior}!!')
menor = min(lista)
print(f'O menor número é o {menor}!!')
"""

## Correção Substituindo informações ###

"""
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

# Descobrir o menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor número é o {menor}')

# Descobrir o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é o {maior}')
"""

### Desafio 34 ### - Correto

# Escreva um programa que pergunte o salario de um funcionario
# Calcule o aumento || (use if)
# Salarios superiores a R$ 1250,00, calcule 10%
# Para inferiores ou iguais, Calcule 15%
"""
salario = float(input('Digite seu Salario: R$'))

if salario > 1250.00:
   nvsalario = salario + (salario * 15 /100)
   print('O seu salario novo é R$ {:.2f}!!'.format(nvsalario))
else:
   soma2 = (salario * 0.15)
   nvsalario2 = (salario + soma2)
   print('O seu salario novo é R$ {:.2f}!!'.format(nvsalario2))
"""

### Desafio 35 ### - Correto

# Desenvolva um programa que leia 3 comprimentos
# Diga se pode fazer um triangulo

# a = float(input('Digite um comprimento:'))
# b = float(input('Digite um comprimento:'))
# c = float(input('Digite um comprimento:'))

# if (a + b < c) or (a + c < b) or (b + c < a):
#        print('Não, é um triangulo')
# else:
#    print('Sim, é um triangulo')