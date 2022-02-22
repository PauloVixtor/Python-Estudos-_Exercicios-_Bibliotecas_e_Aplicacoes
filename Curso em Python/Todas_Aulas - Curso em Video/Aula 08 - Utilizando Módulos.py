# Para estudar as bibliotecas e possibildiades de uso

# https://docs.python.org/pt-br/3/library/index.html ou entrar em python.org> DOC> referencias de biblioteca


# Para importar uma biblioteca

# Existem duas formas

# import(biblioteca) - importa tdoas as funcionalidades de uma biblioteca
# from(biblioteca)import(algo especifico) - importa algo em especifico de funcionalidade dessa biblioteca.

#Exemplos de bibliotecas

# biblioteca (math) funcionalidades de matematica

#Ceil - arredonda para cima um valor.
# Floor - arredonda para baixo um valor.
# trunc - elimina um valor da virgula pra frente sem arredondar o valor
# pow - faz a função de potencia.
# sqrt - faz a função de raiz quadrada.
# factorial - faz a função de multiplicar um valor pelo mesmo.

# biblioteca de matematica

# importar tudo desse biblioteca exemplo

# import math
# num = int(input('Digite um valor: '))
# raiz = math.sqrt(num)
# print('A raiz quadrada de {} e igual à {}'.format(num, math.ceil(raiz))) # arredondo para cima
# print('A raiz quadrada de {} e igual à {}'.format(num, math.floor(raiz))) # arredonda para baixo
# print('A raiz quadrada de {} e igual à {:.2f}'.format(num, raiz))

# importar algo especifico da biblioteca

# from math import sqrt, ceil, floor, trunc

# num = int(input('Digite um número: '))
# raiz = sqrt(num)
# print('A raiz quadrada de {} e igual à {}'.format(num, ceil(raiz)))
# print('Arredondando para baixo o valor e igual {} e ignorando depois da virgula {}'.format(floor(raiz), trunc(raiz)))

# Para estudar as bibliotecas e possibildiades de uso

# https://docs.python.org/pt-br/3/library/index.html ou entrar em python.org> DOC> referencias de biblioteca

# Exemplo de biblioteca de numeros randomicos

# Função random.random( faz um numero aleatorio de 0 a 1)
# import random
# num = random.random()
# print('Seu numero é: {}'.format(num))

# Função random.randint( faz um numero aleatorio inteiro)

# from random import randint
# num = randint(1, 100)
# print('Seu numero é: {}'.format(num))

# Como estudar bibliotecas criadas por outros desenvolvedores

# atraves do link: https://pypi.org/
# Exemplo import emoji = para mostrar emojis
# Para isso deve ser baixado na maquina coloque o nome da biblioteca Ex: import emoji (depois clique no icone vermelho, install packpage emoji)

# import emoji
# print(emoji.emojize('Ola, mundo!! :joy:', use_aliases=True))

# Para procurar os modulos installados clicar em File> setting > projeto > python preferencias.
# botão + procura um novo modulo para adicionar
# botão - desinstalar

