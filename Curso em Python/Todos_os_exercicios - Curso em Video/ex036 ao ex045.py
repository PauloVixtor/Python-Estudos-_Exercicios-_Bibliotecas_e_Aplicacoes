### Desafio 36 ### - Correto

# 36 - Escreva um programa para aprovar um emprestimo
# Deve perguntar o valor da casa
# Deve pergunatr os salario da pessoa
# Deve perguntar em quantos anos ele vai pagar

# Calcule o emprestimo mensal
# Não pode execer 30% do salario
# caso passe de 30% ele e negado
"""
preco_casa = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual é o seu salario atual?: '))
anos = int(input('Em quantos anos pretende pagar?: '))

parcela = salario * 0.3
meses = anos * 12
emprestimo = (preco_casa / meses)
print('O valor de 30% do seu salario atual é R${:.2f}!!'.format(parcela))
print('A quantidade de meses que você pagará é {} meses.'.format(meses))
print('O emprestismo custará R${:.2f}.\n\n'.format(emprestimo))

if emprestimo <= parcela:
    print('Parabéns seu emprestimo foi concedido!!')
    print('A parcela será de {:.2f}'.format(emprestimo))
elif emprestimo > parcela:
    print('Desculpe, seu emprestimo foi negado!!')
    print('Motivo: 30% do seu salario de R${:.2f} não consegue pagar a parcela do emprestimo de R${:.2f}!!'.format(parcela, emprestimo))
"""

### Desafio 37 ### - olhar resposta

# Escreva um programa que leia um número inteiro e peça para ele escolher uma forma de conversão

# 1 para binario
# 2 para octal
# 3 para Hexadecimal
"""
num = int(input('Digite um número inteiro: '))
print('''\nEscolha uma das Bases para Conversão: \n
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal\n''')
opcao = int(input('Digite sua decisão: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}!!'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}!!'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}!!'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente!!')
"""

### Desafio 38 ### - Correto

# Escreva um programa que leia dois numeros inteiros

# compare eles e escreva três mensagem
# O primeiro e maior?
# O segundo e maior?
# não existe maior porque dois são iguais?

"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 > n2:
    print(f'O priemiro é o maior, no caso {n1} e o menor é o {n2}!!')
elif n2 > n1:
    print(f'O segundo é o maior, no caso {n2} e o menor é o {n1}!!')
elif n1 == n2:
    print(f'O primeiro é o segundo tem o mesmo valor, no caso {n1}!!')
"""

### Desafio 39 ### - Correto

# Faça programa que leia o ano de nascimento de uma pessoa e informe:

# Se ele ainda vai se alistar no exercito
# Se é a hora de alistar
# Se já passou o tempo de se alistar

# o programa também deve mostrar o tempo que passou ou vai passar para ele se alistar
"""
nasc = input('Digite sua data de nascimento: ')
ano_atual = 2021
ano_nasc = nasc.split('/')
idade = int(ano_nasc[2])
calcular_idade = ano_atual - idade

if calcular_idade < 18:
    print('Você ainda vai se alistar!!')
    falta_alistar = 18 - calcular_idade
    print(f'Faltam {falta_alistar} anos para você se alistar!!')
elif calcular_idade == 18:
    print('Está na hora de se alistar!!')
elif calcular_idade > 18:
    print('Já passou a hora de você se alistar!!')
    passou_alistar = calcular_idade - 18
    print(f'Você precisava ter se alistado à {passou_alistar} anos atrás, tenha mais atenção!!!')
"""
## Revisão ##
"""
ano = int(input('Digite o ano do seu nascimento: '))
ano_atual = 2021
calcular_idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em 2021.'.format(ano, calcular_idade))
"""

### Desafio 40 ### - Correto

# Cria um porograma que leia duas notas do aluno e calcule a media da nota

# se for abaixo de 5 reprovado
# se for de 5 ou 6.9 recuperação
# se for maior ou igual a 7 aprovado
"""
n1 = float(input('Digite a sua nota da p1: '))
n2 = float(input('Digite a sua nota da p2: '))
media = (n1 + n2) / 2

if media <= 4.9:
    print(f'\nA sua média final foi {media}, você está repovado!!')
elif media >= 5 and media <= 6.9:
    print(f'\nA sua média final foi {media}, você está de recuperação!!')
elif media >= 7:
    print(f'\nA sua média final foi {media}, você está aprovado!!')
"""
## Revisão ##
"""
n1 = float(input('Digite a sua nota da p1: '))
n2 = float(input('Digite a sua nota da p2: '))
media = (n1 + n2) / 2

if media < 5:
    print('\nA sua média final foi {:.1f}, você está repovado!!'.format(media))
elif media >= 5 and media <= 6.9:
    print('\nA sua média final foi {:.1f}, você está de recuperação!!'.format(media))
elif media >= 7:
    print('\nA sua média final foi {:.1f}, você está aprovado!!'.format(media))
"""

### Desafio 41 ### - Correto

# Crie um programa que leia o nascimento de um atleta e diga sua categoria, de acordo com a idade:

# Até 9 anos: Mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# até 20 anos: senior
# acima : master
"""
ano = int(input('Digite o ano do seu nascimento :'))
idade = 2021 - ano

if idade <= 9:
    print(f'Você tem {idade} anos,\n Você competirá: no Mirim!!')
elif idade >= 10 and idade <= 14:
    print(f'Você tem {idade} anos,\n Você competirá no Infantil!!')
elif idade >= 15 and idade <= 19:
    print(f'Você tem {idade} anos,\n Você competirá: no Junior!!')
elif idade == 20:
    print(f'Você tem {idade} anos,\n Você competirá: no Senior!!')
elif idade >= 21:
    print(f'Você tem {idade} anos,\n Você competirá: no Master!!')
"""

### Desafio 42 ### -

# Refaça o programa 35 - corrigido

# Equilatero: todos os lados iguais
# Isolatero: dois lados iguais
# Escaleno: todos lados diferentes

"""
a = int(input('Digite o tamanho do lado do triangulo: '))
b = int(input('Digite o tamanho do lado do triangulo: '))
c = int(input('Digite o tamanho do lado do triangulo: '))

if (a + b < c) or (a + c < b) or (b + c < a):
       print('Não, é um triangulo!')
else:
   print('\nSim, esses valores formam um triangulo', end='')
   if a == b == c:
       print(' Equilatero!')
   elif a != b != c != a:
       print(' Escaleno!')
   else:
       print(' Isolatero!')"""

### Desafio 43 ### - Correto

# Leia o peso e a altura de uma pessoa e calcule o seu IMC

# Usnao a tabela a baixo:
    # abaixo de 18.5: abaixo do peso
    # entre 18.5: peso ideal
    # entre 25 até 30: Sobrepeso
    # acime de 40: Obesidade morbida
"""
peso = float(input('Digite o seu Peso atual: '))
altura = float(input('Digite a sua altura atual: '))

imc = peso/(altura ** 2)
print('\nO seu IMC é igual à {:.2f}!!\n'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso!')
elif 18.5 >= imc < 25:
    print('Você está no peso ideal!')
elif 25 >= imc < 30:
    print('Você está sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade morbida!')"""


### Desafio 44 ###

# Pegue um produto qualquer e calcule o valor a ser pago pelo produto

# Considerando:

# Preço normal
# Condição de pagamento

# A vista: Dinheiro ou Cheque = 10% de desconto
# A vista: no cartão = 5% de desconto
# Em até 2x: no cartão = preço normal
# Em 3x ou mais: no cartão = 20% de juros
"""
tv = 2000
mesa = 1500
armario = 3000
sofa = 4000

lista = ['tv'.title(), 'mesa'.title(), 'armario'.title(), 'sofa'.title()]
lista_p = str(lista).strip().title()

print(f'Esses são os produtos a venda: {lista}\n')
produto = str(input('Digite o produto que deseja comprar: ')).strip().title()
if produto in lista_p:
    print('Sim!')

    dinheiro = (10/100)
    cheque = (10/100)
    cartao = (5/100)
    cartao_x3 = (20/100)

    lista_pag = ['dinheiro'.title(), 'cheque'.title(), 'cartao'.title(), 'cartao_x2'.title(), 'cartao_x3'.title()]
    lista_pag_tratado = str(lista_pag).strip().title()
    print(f'Essas são as formas de pagamento: {lista_pag}\n')
    esc_pagamento = str(input('Escolha o pagamento: ')).strip().title()
    print('\n')
    if esc_pagamento in lista_pag_tratado:

        if produto == lista[0]:
            if esc_pagamento == lista_pag[0]:
                tv_desconto = tv * dinheiro
                tv_dinheiro = tv - tv_desconto
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[0], tv, tv_dinheiro))
            if esc_pagamento == lista_pag[1]:
                tv_desconto2 = tv * cheque
                tv_cheque = tv - tv_desconto2
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[0], tv, tv_cheque))
            if esc_pagamento == lista_pag[2]:
                tv_desconto3 = tv * cartao
                tv_cartao = tv - tv_desconto3
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[0], tv, tv_cartao))
            if esc_pagamento == lista_pag[3]:
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[0], tv))
            if esc_pagamento == lista_pag[4]:
                tv_juros = tv * cartao_x3
                tv_mais = tv_juros + tv
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[0], tv_mais))

        if produto == lista[1]:
            if esc_pagamento == lista_pag[0]:
                desconto_mesa = mesa * dinheiro
                mesa_dinheiro = mesa - desconto_mesa
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[1], mesa, mesa_dinheiro))
            if esc_pagamento == lista_pag[1]:
                desconto_mesa2 = mesa * cheque
                mesa_cheque = mesa - desconto_mesa2
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[1], mesa, mesa_cheque))
            if esc_pagamento == lista_pag[2]:
                desconto_mesa3 = mesa * cartao
                mesa_cartao = mesa - desconto_mesa3
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[1], mesa, mesa_cartao))
            if esc_pagamento == lista_pag[3]:
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[1], mesa))
            if esc_pagamento == lista_pag[4]:
                mesa_juros = mesa * cartao_x3
                mesa_mais = mesa_juros + mesa
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[1], mesa_mais))

        if produto == lista[2]:
            if esc_pagamento == lista_pag[0]:
                desconto_ar = armario * dinheiro
                armario_dinheiro = armario - desconto_ar
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[2], armario, armario_dinheiro))
            if esc_pagamento == lista_pag[1]:
                desconto_ar2 = armario * cheque
                armario_cheque = armario - desconto_ar2
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[2], armario, armario_cheque))
            if esc_pagamento == lista_pag[2]:
                desconto_ar3 = armario * cartao
                armario_cartao = armario - desconto_ar3
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[2], armario, armario_cartao))
            if esc_pagamento == lista_pag[3]:
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[2], armario))
            if esc_pagamento == lista_pag[4]:
                armario_juros = armario * cartao_x3
                armario_mais = armario_juros + armario
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[2], armario_mais))

        if produto == lista[3]:
            if esc_pagamento == lista_pag[0]:
                desconto_sofa = sofa * dinheiro
                sofa_dinheiro = sofa - desconto_sofa
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[3], sofa, sofa_dinheiro))
            if esc_pagamento == lista_pag[1]:
                desconto_sofa2 = sofa * cheque
                sofa_cheque = sofa - desconto_sofa2
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[3], sofa, sofa_cheque))
            if esc_pagamento == lista_pag[2]:
                desconto_sofa3 = sofa * cartao
                sofa_cartao = sofa - desconto_sofa3
                print('O produto é uma {}, o valor era R${:.2f} ficou por R${:.2f}!!'.format(lista[3], sofa, sofa_cartao))
            if esc_pagamento == lista_pag[3]:
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[3], sofa))
            if esc_pagamento == lista_pag[4]:
                sofa_juros = sofa * cartao_x3
                sofa_mais = sofa_juros + sofa
                print('O produto é uma {}, o valor é R${:.2f}!!'.format(lista[3], sofa_mais))

    else:
        print('Não, existe essa forma de pagamento!')
else:
    print('Não, existe esse produto!')
"""


### Desafio 45 ### - Correto

# Crie um programa que faça um computador jogar jokenpo
"""
import random
from time import sleep
from PIL import Image, ImageFilter

lista = ['Pedra', 'Tesoura', 'Papel']
esc_computador = random.choice(lista)
print(f'Essa é a lista: {lista}\n')

esc_jogador = str(input('Escolha um dos Três a cima: ')).strip().title()

print('AGUARDANDO ESCOLHA DA MAQUINA.....')
sleep(2)
print('==============JOKENPÔ==============')
print('Você escolheu!' + ' X ' 'A maquina escolheu!')
print(f'        {esc_jogador}' + '    X    ' + f'{esc_computador}')
if esc_computador == lista[0]:
    if esc_jogador == 'Pedra':
        print('     Foi Empate!')
    if esc_jogador == 'Tesoura':
        print('     A Maquina te derrotou!!')
    if esc_jogador == 'Papel':
        print('     Vitória do jogador!!')
if esc_computador == lista[1]:
    if esc_jogador == 'Pedra':
        print('     Vitória do jogador!!')
    if esc_jogador == 'Tesoura':
        print('     Foi Empate!')
    if esc_jogador == 'Papel':
        print('     A Maquina te derrotou!!')
if esc_computador == lista[2]:
    if esc_jogador == 'Pedra':
        print('     A Maquina te derrotou!!')
    if esc_jogador == 'Tesoura':
        print('     Vitória do jogador!!')
    if esc_jogador == 'Papel':
        print('     Foi Empate!')
print('===================================')"""

## Revisão ##
"""
import random
from time import sleep
print("Escolha um desses a baixo para jogar:
[1] Pedra
[2] Tesoura
[3] Papel
")


esc_jogador = str(input('Digite a sua escolha: ')).strip().title()

lista = [1, 2, 3]
esc_computador = random.choice(lista)

print('AGUARDANDO ESCOLHA DA MAQUINA.....')
sleep(2)
print('==============JOKENPÔ==============')
print('Você escolheu!' + ' X ' 'A maquina escolheu!')
print(f'        {esc_jogador}' + '    X    ' + f'{esc_computador}')
if esc_computador == 1:
    if esc_jogador == 1:
        print('     Foi Empate!')
    if esc_jogador == 2:
        print('     A Maquina te derrotou!!')
    if esc_jogador == 3:
        print('     Vitória do jogador!!')
if esc_computador == lista[1]:
    if esc_jogador == 1:
        print('     Vitória do jogador!!')
    if esc_jogador == 2:
        print('     Foi Empate!')
    if esc_jogador == 3:
        print('     A Maquina te derrotou!!')
if esc_computador == lista[2]:
    if esc_jogador == 1:
        print('     A Maquina te derrotou!!')
    if esc_jogador == 2:
        print('     Vitória do jogador!!')
    if esc_jogador == 3:
        print('     Foi Empate!')
"""