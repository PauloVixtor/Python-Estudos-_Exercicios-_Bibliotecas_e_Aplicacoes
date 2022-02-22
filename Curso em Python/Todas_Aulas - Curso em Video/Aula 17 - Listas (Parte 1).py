### Aula 17 - Listas (Parte 1) ###

# Nessa aula vamos ver como criar, adicionar e trabalhar com uma lista de dados.
# Começa com 0 a lista sempre
# Lista em python são feitas em []
# Vc não consegue substituir um item da lista por uma tupla.
# Mais consegue substituir um item da lista com outra lista.

# Recebe diversas variaveis


# Mostrar algo na lista:

"""
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche[2])                                    # Mostra o 3 item da lista
"""

# Como alterar algo na lista:

"""
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3]='Picole'
print(lanche[3])                                  # Dessa forma vc consegue alterar uma lista ( variavel composta).
"""
########## ADICIONA A LISTA ##########

# Adicionar algo na lista ( APPEND = adiciona)

"""
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche.append('Cookie') # Cria o elemento 4
print(lanche, '\n')"""

# Adicionar algo na lista (INSERT = insere em qualquer local)

    # Ao adicionar em qualquer posição as posições da frente pulam para proximo numero da lista

"""
lanche.insert(0, 'Hot Dog') # Insere intem novo co começo a lista
print(lanche)"""

#######################################
# # # # TEORIA
#######################################

########## APAGA DA LISTA ##########

# Como apagar um item de uma lista ( del = Deletar).

"""
lanche = ['Hot Dog','Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']
del lanche[3]                       # Retira item 3 da lista, no caso a pizza
print(lanche)"""

# Como apagar um item de uma lista ( pop = ele apaga ultimo elemento mais tbm pode apagar qualwuer parte).

"""
lanche = ['Hot Dog','Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']
lanche.pop(3)                   # Retira item 3 da lista, no caso a pizza
print(lanche)"""

# Como apagar um item de uma lista (remove = removeritem da lista)

    # #lemina pelo conteudo, reposiciona a lista

"""
lanche = ['Hot Dog','Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']
lanche.remove('Pizza')              # Retira item pizzada lista.
print(lanche)"""


# Usando IF para verificar e pagar algo na lista

"""
lanche = ['Hot Dog','Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']
if 'Pizza' in lanche:               # Apenas apaga da lista se estiver dentro dessa lista
    lanche.remove('Pizza')
    print(lanche)"""

########## CRIANDO LISTA COM RANGE ##########

# Como cirar uma lista dentro do Range

            # Cria uma lista chamada valores

"""
valores = list(range(4,11))    # Cria lista de 4 até 10
print(valores)"""


######### COMO ORDENAR A LISTA #########

# Como ordenar de forma crescente a lista

"""
valores = [4, 3, 6, 7, 8, 2, 5]
valores.sort() # Ordena valores da lista
print(valores)"""

# Como ordenar de forma decrescente a lista ( ou ao inverso) e contar numero na lista

""""
valores = [4, 3, 6, 7, 8, 2, 5]
valores.sort(reverse=True)          # Ordena valores da lista
print(valores, '\n')
print(len(valores))                 # Quantos elementos
"""

############################
# # # # Pratica
############################

# Exemplo alterar lista:

"""
num = [1, 2, 4, 4]
num[2] = 3 # alterou o 4
print(num)"""

# Exemplo como não adionar valores

"""
num = [1, 2, 4, 4]
num[4] = 7
print(num)"""

# Adicionando com Apend:

"""
num = [1, 2, 4, 4]
num.append(5) # adicionar valor ao final
print(num)"""

# Exemplo para ordenar:

"""
num = [2, 8, 6, 4]
num.sort()
print(num)"""

# Exemplo para ordenar Reversa:

"""
num = [2, 8, 6, 4]
num.sort(reverse=True)
print(num)"""

# Exemplo de contagem de lista:

"""
num = [2, 8, 6, 4]
print(f'Essa lista tem {len(num)}')"""

# Exemplo inserir em alguma parte da lista:

"""
num = [2, 8, 6, 4]
num.insert(2, 0)
print(f'Essa lista tem {len(num)}')"""

# Exemplo apagar com pop:

"""
num = [2, 8, 6, 4]
num.pop(2)
print(f'Essa lista tem {len(num)}')"""

# Exemplo como eliminaro a primeira ocrrencia do elemento:

                 # Eh possivel apagar os demais com laços

"""
num = [2, 8, 6, 4]
num.remove(2)
print(num)"""

# Exemplo usar IF com remover:

"""
num = [2, 8, 6, 4]
if 2 in num:
    num.remove(2)
    print(num)"""

# Exemplo deixar mais visivel com FOR:

"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores, '\n')

for v in valores:
    print(f'{v}...', end='')"""

# Exemplo ver a posição e enumerar.

"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores, '\n')

for c, v in enumerate(valores):
    print(f'A posição {c + 1} o valor é {v}!')
print('FIM!')"""

# Exemplo de como o usuario pode informar esses valores e isso pode ser adicionado em uma lista:

"""
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite o valor: ')))
print(valores)"""

# Exemplo como ele mostra a mesma lista

"""
a = [2, 3, 4, 5]
b = a
print(a)
print(b)"""

# Exemplo como ele mexe nas duas listas caso sejam referencias uma na outra.

"""
a = [2, 3, 4, 5]
b = a
b[2] = 7
print(a)
print(b)"""


# Exemplo lista recebe apenas valores da outra:

"""
a = [2, 3, 4, 5]
b = a[:]
b[2] = 7
print(a)
print(b)"""