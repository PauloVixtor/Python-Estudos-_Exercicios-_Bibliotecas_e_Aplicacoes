## ------------- Desafios do 22 ao 27 ------------- ##

## --- Exercicio 22 --- ##

### Crie um programa que leia o nome completo de uma pessoa ###

nome = 'Paulo Victor Caminha de Oliveira'

# Todas maiusculas?

# print('Seu nome minuscula é {}'.format(nome.upper()))

# Todas minusculas?

# print('Seu nome minuscula é {}'.format(nome.lower()))

# Quantas letras ao tudo sem contar os espaços?

# juntar = nome.replace(' ', '')
# print('Seu nome tem {} de letras!!'.format(len(juntar)))

# Outra forma de fazer!!

# novo = str(input('Digite seu nome: ')).strip()
# print('Seu nome tem {} de letras!!'.format(len(novo) - novo.count(' ')))
# print('Seu primeiro nome tem {} letras!!'.format(nome.find(' ')))

# Quantas letras tem o primeiro nome?

# primeiro = nome.split()
# print(primeiro[0])

# Outra forma de fazer!!

# primeiro2 = nome.split()
# print('Seu nome é {} e ele tem {} letras!!'.format(primeiro2[0], len(primeiro2)))

## --- Exercicio 23 --- ##

# digite um numero de 0 a 9999 e separe por casa decimal

# num1 = str(input('Digite um número de 0 a 9999: '))
# print('O número escolhido foi {}!!'.format(num1))
# print(' ')
# mudar = ' '.join(num1)
# separado = mudar.split()
# print('Unidade é: {}'.format(separado[3]))
# print('Dezena  é: {}'.format(separado[2]))
# print('Centena é: {}'.format(separado[1]))
# print('Milhar  é: {}'.format(separado[0]))

####################################### Correção!! ########################################3

# num2 = int(input('Digite um número de 0 a 9999: '))
# un = num2 // 1 % 10
# de = num2 // 10 % 10
# cen = num2 // 100 % 10
# mi = num2 // 1000 % 10
# explicação: ele fraciona o numero informado em um calculo.

# print('Unidade é: {}'.format(un))
# print('Dezena  é: {}'.format(de))
# print('Centena é: {}'.format(cen))
# print('Milhar  é: {}'.format(mi))


## --- Exercicio 24 --- ##

# Crie um programa que leia o nome de uma cidade e diga se ela começa com "Santo"?

# cidade = str(input('Digite o nome da sua Cidade : ')).strip()
# inicia = cidade.title()
# separe = inicia.split()
# duvida = 'Santo' in separe[0]
# print(duvida)
# if (duvida) == True:
#    print('Sim começa com "Santos"!!')
# else:
#    print('Não começa com "Santos"!!')

# Outra forma de fazer!!

# cidade = str(input('Digite o nome da sua Cidade : ')).strip()
# print(cidade[:5].upper() == 'SANTO')

## --- Exercicio 25 --- ##

# Crie um programa que leia o nome de uma pessoa e diga se o nome dela tem "silva"?

# nomepes = str(input('Digite seu nome: ')).strip()
# inicial = nomepes.title()
# duvidas = 'Silva' in inicial
# print(inicial)
# print(duvidas)
# if (duvidas) == True:
#    print('Seu nome contém Silva!!')
# else:
#    print('Seu nome não contém Silva!!')

# Outra forma de fazer!!

# nomepis = str(input('Digite seu nome: ')).strip()
# print('Seu nome contém silva? {}'.format('silva' in nomepis.lower()))

## --- Exercicio 26 --- ##

# Crie um programa que leia qualquer frase

# frase1 = str(input('Digite um frase qualquer: ')).strip().lower()

# quantas vezes aparece a letra A

# letra = str(input('Digite uma letra: ')).strip()
# print('São {} de letras {}!!!'.format(frase1.count(letra.lower()), letra.title()))

# Em que posição ela aparece a primera vez

# print('A posição que a letra {} aparece é a {}!!'.format(letra.title(), frase1.find(letra) + 1))

# cont = len(frase1)
# print(frase1.count('a', 0, cont))

# Em que posição ela aparece a ultima vez

# print('A ultima posição que a letra {} aparece é a {}!!'.format(letra.title(), frase1.rfind(letra) + 1))

## --- Exercicio 27 --- ##

# Crie um programa que leia o nome de uma pessoa e diga o primeiro e ultimo nome?

# nome2 = str(input('Digite seu nome completo: ')).strip().title()
# separou = nome2.split()
# contou = len(separou)
# print('Muito Prazer em te conhecer {}!!'.format(nome2))
# print('Seu primeiro nome é {}'.format(separou[0]))
# print('Seu ultimo nome   é {}'.format(separou[contou - 1]))

num1 = str(input('diga:')).strip()
print(num1.upper())