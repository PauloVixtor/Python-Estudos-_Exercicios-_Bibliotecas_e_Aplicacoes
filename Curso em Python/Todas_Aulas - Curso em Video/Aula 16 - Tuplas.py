### Aula 16 - Tuplas ###

# Nessa aulas vamos ver como funciona uma tupla, ou seja, uma variavel composta.(Parecido com uma lista)

# Com as tuplas vc recebe diversas variaveis dentro de apenas uma.
# Utilizando as tuplas vc consegue adicionar variaveis novas, sem apagar as antigas.
# Amazenando assim diversos valores, eles são armazenados em indices de 0 até a aultima variavel.
# Tuplas são imutaveis, ou seja, elas não podem ser alteradas.

## Estrutura de repetição ##

# tuplas também podem ser usados em FOR ou WHILE para percorrer a lista.

# Exemplo:

# Lanche = [0, 1, 2 ,3]
# Mostrar(lanche[1])


## Teoria ##

# Para mostrar um lanche

# Lanche = [ 'hot dog', 'suco', 'pizza', 'pudim']
# print(lanche[2])
# Pizza


# Para mostrar o Lanche de 0 até 1.( Ele exclui o numero 2 porque ele criterio de parada)

# Lanche = ('hot dog', 'suco', 'pizza', 'pudim')
# print(lanche[0:2])
# ('hot dog', 'suco')

# Para mostrar lanche do 1 até final da tupla.( Ele não mostra os numeros antes do 1)

# Lanche = ('hot dog', 'suco', 'pizza', 'pudim')
# print(lanche[1:])
# ('suco', 'pizza', 'pudim')

# Para mostrar o ultimo elemento

# Lanche = ('hot dog', 'suco', 'pizza', 'pudim')
# print(lanche[-1:])
# ('pudim')


# Como ler o comprimento da tupla.

# Lanche = ('hot dog', 'suco', 'pizza', 'pudim')
# print(len(lanche))
#       4

# Como criar uma estrutura de repetição para mostrar um itens da tupla de cada vez com menos linhas.

# Lanche = ('hot dog', 'suco', 'pizza', 'pudim')
# for c in lanche:
#    print(c)
# 'hot dog' \n
# 'suco' \n
# 'pizza' \n
# 'pudim'


## Pratica ##

# Toda tupla ela é entre parenteses, mais tem versos que não precisa. Pode ser inciada com tupla (), lista [] ou dicioanrio {}.
# Pode até tirar o paretese da tupla.
# Tuplas começam com número 0 - ATENÇÃO!!!.
# Ao suar numeros negativas a tupla será percorrida ao contrario.
# tuplas imutaveis
# No python tuplas podem usar qualquer string estando na mesma tupla.
# Não pode deletar um item da tupla, mais pode deletar toda a tupla.


# Mostrando tupla.
"""
# lanche = 'Hot dog,', 'Suco', 'Pizza', 'Pudim'
lanche = ('Hot dog,', 'Suco', 'Pizza', 'Pudim')
print(lanche)"""

# Mostrar tupla 0, 1, 2, 3:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[0])"""

# Mostrar tupla -0, -1, -2, -3:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])
print(lanche[-0])"""

# Mostrar elemento de certo numero ao outro( lembrando que criterio de parada é ultimo numero).

"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])"""

# De um elemento até o final:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:])"""

# Do elemento inicial até um determinado (Lembrando que ultimo é o criterio de parada):
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])
print(lanche[-2:])"""

# Tuplas imutaveis:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
lanche[1] = 'Refri'
print(lanche[1])
# print(lanche[1].replace('Refrigerante'))"""

# Laço de repetição com tupla:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Estou Satisfeito!')"""

# Contagem de tuplas:

"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim', 'batata')
print(len(lanche))"""

# Usando um For in Range com tuplas:

"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim', 'batata')

for c in range(0, len(lanche)):
    print(f'Vou comer {lanche[c]} na posição {c}!\n')
    # print(lanche[c], end=' - ')
    # print(c, '\n')
print('Estou Satisfeito!')"""

# Usando For par enumerar a tupla:

"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim', 'batata')

for c in enumerate(lanche):
    print(f'Na posição {c}!\n')

print('Estou Satisfeito!')"""

# Usando for para mostrar posição e enumerar uma tupla:
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim', 'batata')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} / Na posição {pos}!\n')

print('Estou Satisfeito!')"""


# Para organziar a tupla( Usando sorted):
"""
lanche = ('Hot dog', 'Suco', 'Pizza', 'Pudim', 'Batata')
print(sorted(lanche)) # Não altera a tupla apenas coloca em ordem."""

# Como adicionar uma tupla a outra, criando assim uma nova:
"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Ordem importa aqui.
print(c)"""

# Quantas vezes aparece um numero, uma palavra ou algo na tupla:
"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Ordem importa aqui.
print(c.count(5))"""

# Em qual posição está uma certa palavra, numero ou item:
"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # Ordem importa aqui.
print(c)
print(c.index(2)) # Pega a primeira ocorrencia
print(c.index(2, 4)) # numero desejado e começa na posição desejada."""

# No python tuplas podem usar qualquer string estando na mesma tupla.
"""
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)"""

# Como apagar uma tupla:
"""
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)"""
