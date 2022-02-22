### Aula 14 - Estrutura de repetição while ###

# Nessa aula iremos ver o laço sem controle ( Quando não se sabe a quantidade de vezes que se deve repetir algo).

# While = Repetição não for igual a o resultado ele continua o evento.

## Teoria ##

# Exemplo:

# While False:   // While funcionará enquanto o resultado for FALSE.
#    Passo   // Tudo aqui dentro está dentro do while
# Pegar        // Saindo do laço.

# Exemplo da maça:

# While not MAÇÃ:
#   if chao == True:
#       Passo
#   if buraco == True:
#       Pular
#   if Moeda == True:
#       Pegar moeda
# // Se maçã for igual a TRUE então ele sai do laço.
# Pega Maçã

## Pratica ##

# Fazendo esse mesmo teste com WHILE.

# EXEMPLOS:

# FOR
"""for c in range(1,10):
    print(c)
print('FIM!')"""

# WHILE
"""
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')"""

# Caso você não saiba o limite utilize o WHILE.

# EXEMPLOS 2:

"""
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM!')"""

"""
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')"""

# Ele vai rodar o programa enquanto n estiver diferente de 0, ou seja, um ponto de parada.

# Exemplos com str:

"""
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar: [S/N]: ')).upper()
print('FIM!')"""

# Exemplo 3

"""
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Se for diferente de 0.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'A quantidade par é {par}!!')
print(f'A quantidade impar é {impar}!!')
print('Acabou!')"""

# Exemplos

'''for c in range(1, 10):
    print(c)
Print('Fim')'''

# Estrutura de repetição para pegar um valor inicial e replicar ele até menor de 10

# c = 1
# while c < 10:
#    print(c)
#    c = c + 1
# print('Fim')

# Enquanto não digitar 0 o codigo não para

# n = 1
# while n != 0:
#    n = int(input('Digite um número: '))
# print('Fim')

# Enquanto você quiser continuar e apenas digitar S

# r = 'S'
# while r == 'S':
#    n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar [S/N]: ')).upper()
# print('Fim')

# contagem de pares e impares antes de chegar ao número 0

# n = 1
# par = impar = 0
# while n != 0:
#    n = int(input('Digite um valor: '))
#    if n != 0:
#        if n % 2 == 0:
#            par += 1
#        else:
#            impar += 1
# print('Você digitou número {} pares e números foram impares {}.'.format(par, impar))
# print('Fim')
