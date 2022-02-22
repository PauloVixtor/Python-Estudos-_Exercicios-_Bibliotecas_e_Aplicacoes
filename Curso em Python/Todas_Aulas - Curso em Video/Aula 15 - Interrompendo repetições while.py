### Aula 15 - Interrompendo repetições while ###

# Nessa aula iremos ver os interruptores de WHILE. ( Interrupção de laço).

# Break = Parar o laço e continuar o codigo.

## Teoria ##

# Exemplo da maça com trofeu:

# While True:       // Laço de repetição inifinita, até o criterio de parada.
#   if chao == True:
#       Passo
#   if buraco == True:
#       Pular
#   if Moeda == True:
#       Pegar moeda
#   if Trofeu == True:
#       pular
#       Break       // Interrompe o laço. Saindo do laço de repetição.
# Pega

## Pratica ##

# Laço infinito:

"""
cont = 1
while True: # Laço infinito.
    print(cont, '', end='')
    cont+=1"""

# Exemplo 2:
"""
n = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    if cont >= 5:
        break
print(cont)"""

# Exemplo 3:
"""
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:     # Esse e o novo criterio de parada, não sendo necessario colocar no while.
        break        # Para a estrutura de repetição
    s += n           # Apenas vai somar se não for 999.
print('A soma vale {}'.format(s))"""

# Exemplo 4:
"""
nome = 'josé'
idade = 33
print(f'O {nome} tem {idade} anos') # Atual.
print('O %s tem %d anos' % (nome, idade)) # Jeito antigo de se escrever.
"""

## Criterio de parada atuais ##

### break: é quebrar, quebra (ou interrompe) o fluxo natural do programa

# Break Exemplo:
"""
n = 0
while True:
    if n == 10:
        break
    n += 1
    print(n)
print('Acabou!')
"""

### continue: é continuar, ou seja, continua o fluxo natural do ciclo


# A diferença entre usar a instrução continue, em vez de uma instrução break,
# é que o nosso código continuará apesar da interrupção quando a variável number for avaliada como equivalente a 5.
# Vamos ver nosso resultado:

"""
numero = 0

for numero in range(10):
    if numero == 5:
        continue    # continue aqui, ele ignora o número se for igual a 5, ou seja, continua o que está fazendo.

    print('Numero é ' + str(numero))

print('Fora do laço!')"""

# A instrução continue faz com que um programa pule certos fatores que surjam dentro de um loop,
# mas depois continuem pelo restante do loop.



### pass: é passar, ou seja, deixa passar.


# A instrução pass que ocorre após a instrução condicional if está dizendo ao programa para continuar executando o loop
# e ignorar o fato de que a variável number é avaliada como equivalente a 5 durante uma das iterações.

# Vamos executar o programa e verificar o resultado:
"""
numero = 0

for numero in range(10):
    if numero == 5:
        numero = 5 + 2
        pass    # continue aqui, ele ignora o número se for igual a 5, ou seja, continua o que está fazendo.

    print('Numero é ' + str(numero))

print('Fora do laço!')"""

# A instrução pass pode criar classes mínimas, ou agir como um espaço reservado enquanto estamos trabalhando em novos
# códigos e pensando em um nível algorítmico antes de construir detalhes.

# Conclusão
# As instruções break, continue e pass em Python permitem que você use loops for e while com maior
# efetividade em seu código.