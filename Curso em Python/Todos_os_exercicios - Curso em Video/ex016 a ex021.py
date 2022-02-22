# 16 - Exercicio 1 arredondar numero - correto !!!

# from math import trunc
# num = float(input('Digite um número real:'))
# print('O numéro digitado foi {} e o seu numero inteiro é: {} !!'.format(num, trunc(num)))

# 17 - Calculado o comprimento da hipotenuza - correto!!

#import math

# num1 = int(input('Digite o comprimento do cateto oposto: '))
# num2 = int(input('Digite o cateto adjacente de um triangulo retangulo: '))
# cateto = math.hypot(num1, num2)
# print('O compriemnto da hipotenusa é: {:.2f} '.format(cateto))

# from math import sqrt
# num1 = int(input('Digite o comprimento do cateto oposto: '))
# num2 = int(input('Digite o cateto adjacente de um triangulo retangulo: '))
# hipo = sqrt(num1*num1 + num2*num2)
# print('A hipotenusa é igual à: {:.2f} '.format(hipo))

# 18 - Demostre o tangente, cosseno e seno de um angulo - correto !!

# import math
# num = int(input('Digite o valor do angulo: '))
# sen = math.acosh(num)
# cos = math.asinh(num)
# tan = math.tanh(num)
# print('O valor do angulo é {}\nO seno é igual à {:.2f} !!\nO cosseno é igual à {:.2f} !!\nO tangente é igual à {:.2f} !!'.format(num, sen, cos, tan))

# 19 - Sorteio do nome para apagar a lousa do professor - correto !!

# import random
# aluno1 = str(input('Qual o nome do aluno? : '))
# aluno2 = str(input('Qual o nome do aluno? : '))
# aluno3 = str(input('Qual o nome do aluno? : '))
# aluno4 = str(input('Qual o nome do aluno? : '))
# esc = random.choice([aluno1, aluno2, aluno3, aluno4])
# print('O aluno selecionado foi {}, por favor apague a lousa!!'.format(esc))

#    Primeiro teste

# import random
# alu = random.choice(['red', 'black', 'green', 'white'])
# print('O aluno selecioando foi {}, por favor apague a lousa!!'.format(alu))

# 20 - O professor quer sortear a ordem dos alunos - correto

# import random
# aluno1 = str(input('Qual o nome do aluno? :'))
# aluno2 = str(input("Qual o nome do aluno? :"))
# aluno3 = str(input("Qual o nome do aluno? :"))
# aluno4 = str(input("Qual o nome do aluno? :"))
# lista = [aluno1, aluno2, aluno3, aluno4]
# random.shuffle(lista)
# print('A ordem é: {}'.format(lista))

# random

# from random import shuffle
# alus = 'red black green white'.split()
# shuffle (alus)
# print('A ordem é: {} '.format(alus))

# 21 - Abra um arquivo no computador

# import pathlib


# man = open('C:paulo.v.oliveira\Desktop\TRABALHO\Arquivo Dash Cadastro\Atualizar\Dashbard Cadastro - Fiscal v11.pbix', 'r')


