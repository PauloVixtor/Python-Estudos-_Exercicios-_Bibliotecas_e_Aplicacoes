### Aula 20 - Funções (Parte 1) ###

# Funções = def
# Defenição de função = Em Python, uma função é uma sequência de comandos que executa alguma tarefa e que tem um nome.
# Outra forma de dizer isto é que os parâmetros especificam o que a função necessita para executar a sua tarefa.
# Pode existir qualquer número de comandos em uma função, mas eles tem que ter a mesma tabulação a partir do def.

# Função é um rotina.
# Algumas funções já usadas( print(), len(), int(), input(), float()).
# DEF = Definição de Função.

## Teoria ##

# O comando se repete 6 vezes de print('-' * 30), para isso conseguimos fazer uma função para economizar tempo.
"""
print('-' * 30)
print('     Profissional')
print('-' * 30)
print('-' * 30)
print('     Estudos')
print('-' * 30)
print('-' * 30)
print('     Erro de Sistema')
print('-' * 30)"""

## DEF faz uma rotina, que pode executar um bloco de codigo especifico, sempre que necessario!.

# Toda vez que codigo e executado, e tiver o nome do DEF, ele volta em cima no codigo e executa o bloco e volta ao codigo.
# O programa não executa as suas DEF, a não ser que o nome da DEF seja adicionado ao comando.
"""
def mostra_linha ():
    print('-' * 30)

mostra_linha() # Nome da DEF.
print('     SISTEMA DE ALUNOS    ')
mostra_linha()
mostra_linha()
print('     CADASTRO DOS FUNCIONARIOS     ')
mostra_linha()
mostra_linha()
print('     ERRO D0 SISTEMA  ')
mostra_linha()"""

# Como fazer um bloco executar com variavel que está fora do bloco.
# Executa um bloco e aplica a mensagem dentro dele.

"""
def mensagem(txt): # Função(Parametro) // executa função e chama o parametro
    print('-'* 30)
    print(txt) # Insere o parametro mensagem no bloco.
    print('-'* 30)

mensagem('SISTEMA DE ALUNOS') # mensagem e imprimida dentro da função
mensagem('CADASTRO DOS FUNCIONARIOS')
mensagem('ERRO D0 SISTEMA')"""


#### Pratica ####

## Exemplo sem def
"""
a = 5
b = 5
soma = a + b
print(soma)
a = 6
b = 8
soma = a + b
print(soma)
a = 9
b = 5
soma = a + b
print(soma)"""

## Exemplo usando o DFE:
"""
def soma(a, b):
    print(f'A = |{a}| + B = |{b}| = ', end='')
    s = a + b
    print(f'Resultado é |{s}|')

# Programa Principal

soma(5, 5) # Se não for explicado, o parametro segue a ordem
soma(8, 6)
soma(9, 5)

## Explicando parametros
soma(a=4, b=5) # Nesse caso dizemos que parametro recebe qual valor.
soma(b=5, a=6)"""

# Caos você informa apenas um número o codigo irá dar erro
# soma(1) # Isso porque o codigo precisa ter dois parametros.

## Empacotamento de parametros
# Essa funcionalidade é dificilmente encontra em outra linguagem.
# Permite passar diversos valores e depois descompactar na função. Mesmo sem saber a quantidade final.

## Nesse exmeplo o resultado e uma tupla com diversos numeros // TUPLA.

"""
def contador(* num):
    for valor in num:
        print(f'|{valor}|', end='')
    print(' FIM!')"""

# Contagem de numeros recebidos e mostrar na tela.
"""
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')

# Principal

contador(2, 1, 7)
contador(8, 1)
contador(9, 8, 7, 6)"""

## Lista em funções

# Esse exemplo não é um descompactar por ser uma lista.
"""
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

# Principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)"""

# Descompactar com função por ser uma tupla e soma os valores:


def soma (* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}')


soma(5, 2)
soma(2, 9, 4)