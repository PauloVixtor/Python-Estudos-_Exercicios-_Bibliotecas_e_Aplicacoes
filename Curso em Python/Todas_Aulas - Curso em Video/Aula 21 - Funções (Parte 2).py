### Aula 21 - Funções (Parte 2) ###

## Interactive help - Ajuda interativa, documentação do python.
## docstrings - String de documentação, documentação das funções.
## Argumentos opcionais - É uma variavel não obrigatoria de ser inserida pelo usuario.
## Escopo de variaveis - local em que a variavel vai existir e onde ela não vai mais existir.
## Retorno de resultados - Variveis que recebem um retorno.

### Teorica ###

## Interactive help - Ajuda interativa, documentação do python. ##
"""
import datetime

help(print) # Mostra todas funções e utilizações de Print().
help(len) # Mostra todas funções e utilizações de len().
help(input) # Mostra todas funções e utilizações de input().
help(datetime) # Todas as funções da biblioteca e do comando.
"""
## Como conseguir uma explicação melhor! ##
# Abrir console python a baixo > digitar: help() > Biblioteca, comando, parametro e etc.
# Para sair e só digitar: quit

# Outra forma de conseguir ajuda

"""
print(input.__doc__)
"""

## docstrings - String de documentação, documentação das funções. ##

"""
def contador(i, f, p):
        # Como fazer uma docstrings
        # SÃO 3 ASPAS !!!!!!!!!!!!!!!!!
        ""
        -> Faz a contagem e mostra na tela
        :param i: Inicio da contagem.
        :param f: Fim da contagem.
        :param p: passo da contagem.
        :return: Sem Retorno.
        Função Criada por Paulo Victor aluno do Curso em Video.
        ""
        c = i
        while c <= f:
            print(f'{c}', end='..')
            c += p
        print('FIM!')


contador(0, 100, 10)

help(contador) # Como saber o que faz sua função.
# Toda vez que alguém importar essa função a documentação estará junto para auxiliar a utilizar corretamente o usuario.
"""

## Argumentos opcionais - É uma variavel não obrigatoria de ser inserida pelo usuario. ##

# Caso o valor não seja informado o parametro C será igual a 0.
# c = 0 // Argumento opcional. Porém todas podem ser opcional, nada impede isso.
# também pode ser informado qualquer valor ou texto.

"""
def somar(a=0, b=0, c=0): # c = 0 // Argumento opcional.
        ""
        -> Soma 3 valores e mostra na tela.
        :param a: primeiro valor.
        :param b: Segundo valor.
        :param c: terceiro valor.
        :return: Sem retorno.
        ""
        s = a + b + c
        print(f'A soma é {s}')

somar(3, 2, 5)
somar(8, 4) # Nesse caso se a variavel e opcional, o parametro c não precisa ser informado.
somar(9)
somar(b=4, c=2)

# Nesse caso foi usado um texto na variave opcional.
def nome(azul='cor'):
        print(azul)
nome('Claro')
nome()
"""

## Escopo de variaveis - local em que a variavel vai existir e onde ela não vai mais existir. ##

# Escopo global ou variavel global e a variavel escrita fora de uma função, e funciona em 100% do codigo.
# Escopo local ou variavel local, são variaveis dentro de funções e só funcionam dentro da função.

"""
def teste():
    x = 8 # X é uma variavel local. ( escopo local
    print(f'Na função teste, n vale {n}') # A variavel fora da função funciona na função. ( escopo global).
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}') # Caso tente executar x fora da função, o programa irá dar erro.
teste()"""

"""
# Nesse caso a variavel local não vai mostrar a global, mais sim a variavel A criada dentro da função.

def teste2(b):
    a = 8 # veja que foi criada uma segunda variavel chamada A, porém ela não tem anda haver com a outra variavel.
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')

a = 5 # Primeira Variavel.
teste2(a)
print(f'A fora vale {a}')

# Exemplo 2: de Varivaies globais e locais.
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')
funcao()

n1 = 2
print(f'N1 fora vale {n1}')
"""
### Conceito importante nos exercicios!!!! ####

# Como usar uma variavel global dentro de função:
"""
def teste2(b):
    global a # A variavel a deixa de ser 5 e virá 8.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')

a = 5
teste2(a)
print(f'A fora vale {a}') # A passa a valer 8
"""


## Retorno de resultados - Variveis que recebem um retorno. ##

"""
def somar(a=0, b=0, c=0): # 3 valores opcionais.
    s = a + b + c
    return s # retorna a soma
r1 = somar(3, 2, 5) # Retorna a soma no lugar da variavel
r2 = somar(2, 2)
r3 = somar(4)
print(f'Os calculos deram {r1}, {r2}, {r3}.') # Mostra o retorno.
"""

### Pratica ###

# Ex1: Fatorial de um numero.

"""
def fatorial( num=1):  # 3 - executa função
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: ')) # 1 - numero e digitado
print(f'O fatorial de {n} é igual a {fatorial(n)}') # 2 - fução e chamada // 4 - Retorna resultado ao print"""

# Ex2: Fatorial de varios numeros

"""
def fatorial( num=1):  # 3 - executa função
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')"""

#Ex3: Retornando Verdadeiro ou falso.

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
print(par(num)) # Pega a variavel informada e envia a função, que retorna o resultado.
if par(num):
    print('PAR')
else:
    print('IMPAR')

# Durante os exercicios vai ser explicado diversos tipos de retorno.