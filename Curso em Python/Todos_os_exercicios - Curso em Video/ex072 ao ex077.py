### Desafio 72 ### - Correto
"""
# Crie um programa com uma tupla com numero de 0 a 20 por extenso.
# Seu programava devera ler um número por extenso entre 0 e 20 e mostrar por extenso.

tupla = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
extenso = ('Zero', 'Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Sexto', 'Setimo', 'Oitavo', 'Nono', 'Decimo',
           'Decimo-Primeiro', 'Decimo-Segundo', 'Decimo-Terceiro', 'Decimo-Quarto', 'Decimo-Quinto', 'Decimo-sexto',
           'Decimo-Setimo', 'Decimo-Oitavo', 'Decimo-Nono', 'vigésimo')

escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if escolha not in tupla:
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    else:
        print(f'Você digitou o número: {extenso[escolha]}')
        break
"""

### Desafio 73 ### - Correto

# Crie uma tupla com os 20 colocados da tabela do campeonato Brasileiro de Futebol na ordem de colocação:
# A) Depois motre apenas os 5 primeiros colcoados
# B) Os ultimos 4 colocados da tabela
# C) Uma lista com os times em ordem Alfabetica
# D) Em que posição na tebale está o time da Chapecoense


"""
classificacao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza', 'Fluminense',
                 'Ceará','Internacional','América-MG', 'Santos', 'São Paulo', 'Cuiabá', 'Athletico-PR', 'Atlético-GO',
                 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

print('======================================')
print('       TABELA DE CLASSIFICAÇÃO        ')
for c in range(0, 20, 1):
    print(f'{c + 1} - {classificacao[c]}')
print('======================================\n')
print('Os Classificados para liberdadores 2022 são:')
print(f'A) {classificacao[0:5]}\n')

print('Os rebaixados para Serie B do campeonato em 2022 foram:')
print(f'B) {classificacao[16:20]}\n')
print('A lista do time em ordem alfabetica: ')
print(f'C) Time em ordem alfabetica: {sorted(classificacao)}\n')
print('Qual foi a posição do time do Chapecoense?')
print(f'D) O Chapecoense ficou na {classificacao.index("Chapecoense") + 1}º posição!') # Localiza na tupla
"""

### Desafio 74 ### - Correto

# Crie um programa que vai gerar 5 numeros aleatorios e adiconar eles em uma tupla
# Depois disso mostre a listagem e indique o maior e o menor numero

"""
import random

tupla = ''
max = 0
min = 11
for c in range(0, 5):
    alea = int(random.randint(1, 10))
    if alea > max:
        max = alea
    if alea < min:
        min = alea
    tupla += str(f'{alea}')
    if c != 4:
      tupla += ', '
print(f'Os valores sorteados foram : {tupla}')
print(f'O maior número sorteado foi {max}!')
print(f'O menor número sorteado foi {min}!')
"""

### Desafio 75 ### - Correto

# Desenvolva um programa que leia quatro valores e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes aparece o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares
"""
nove = 0
posicao_3 = 0
pares = ''
pares_c = 0

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))
v4 = int(input('Digite um valor: '))
tupla = v1, v2, v3, v4
for c in range(0, 4, 1):
    if tupla[c] == 9:
        nove += 1
    if tupla[c] == 3:
        posicao_3 = len(tupla[0:c + 1])
    if tupla[c] % 2 == 0:
        pares += str(f'{tupla[c]} ')
        pares_c += 1
if nove == 1:
    print(f'O valor 9 apareceu {nove} vez!!')
elif nove != 1 and nove != 0:
    print(f'O valor 9 apareceu {nove} vezes!!')
elif nove == 0:
    print('O valor 9 não apareceu nenhuma vez!')

if 3 in tupla:
    print(f'O valor 3 apareceu na {posicao_3}º posição!!')
elif 3 not in tupla:
    print('O valor 3 não apareceu em nenhuma posição!!!')
if pares_c != 0:
    print(f'Os valores pares digitados foram(foi): {pares}!')
elif pares_c == 0:
    print('Nenhum número par foi digitado!')
"""

### Desafio 76 ### - Revisão

# Crie uma tupla unica com o nome de produtos e seus respectivos preços na sequencia
# No final organize os daods de forma tabular

"""
lista_prod = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99,
              'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont = len(lista_prod)
print('-------------------------------------------')
print('            LISTAGEM DE PREÇOS             ')
print('-------------------------------------------')
for c in range(0, cont, 2):
    letras = str(lista_prod[c]).count('') - 1
    print(f'{lista_prod[c]}', end='')
    valor = str(lista_prod[c + 1]).count('') - 1
    for espaco in range(letras, 40 - valor):
        print('.', end='')
    if valor == 4:
        print('.', end='')
    if valor == 6:
        print('...', end='')
    print('R$ {:.2f}'.format(lista_prod[c + 1]))
print('-------------------------------------------')
"""
## Revisão ##

"""
lista_prod = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99,
              'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont = len(lista_prod)
print('-------------------------------------------')
print(f'{"LISTAGEM DE PREÇOS":^40}') # Como centralizar
print('-------------------------------------------')
for c in range(0, len(lista_prod)):
    if c % 2 == 0:
        print(f'{lista_prod[c]:.<33}', end='') # Contagem menor que 30 de pontos após a palavra
    if c % 2 == 1:
        print(f'R${lista_prod[c]:>7.2f}') # Contagem de posições maior que 7, com 2 casas decimais.
print('-' * 43) # Multiplicar o que está escrito
"""


### Desafio 77 ### - Correto

# Crie uma tupla com varias palavras( sem acentos)
# Depois disso você deve mostra quais são suas vogais


"""
palavras = ('APRENDER', 'PROGRAMA', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO'
            'PROGRAMADOR', 'FUTURO')
cont_p = len(palavras)
for c in range(0, cont_p):
    print(f'Na palavra {palavras[c]} temos ', end='')
    cont_l = str(palavras[c]).count('') - 1
    for v in range(0,cont_l):
        if str(palavras[c][v]) == 'A':
            print(f'{str(palavras[c][v]).lower()}', end=' ')
        if str(palavras[c][v]) == 'E':
            print(f'{str(palavras[c][v]).lower()}', end=' ')
        if str(palavras[c][v]) == 'I':
            print(f'{str(palavras[c][v]).lower()}', end=' ')
        if str(palavras[c][v]) == 'O':
            print(f'{str(palavras[c][v]).lower()}', end=' ')
        if str(palavras[c][v]) == 'U':
            print(f'{str(palavras[c][v]).lower()}', end=' ')
    print('')
"""