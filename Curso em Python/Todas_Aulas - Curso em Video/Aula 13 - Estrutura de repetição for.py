### Aula 13 - Estrutura de repetição for ###

# Nessa aula iremos ver o laço com varivel de controle.

### For = serve para repetir informações até uma certa quantidade, no caso a quantidade informada.

# Exemplo = for c no range (1,10): // Repetção de 1 até 10.

# Exemplo do personagem pegando a maça:

# laço c no intervalo (1,10): // for c in range(1,10):
#   passo                    //     print('Passo..')
# Pega                      //   print('Pegar')

### For = Pode usar um IF dentro do FOR é um FOR dentro do IF.

# exemplo:

# for c in range(1,10):
# if moeda == True:

# Ou usamos:

# if moeda == True:
#   for c in range(1,10):

# Dependendo da situação.

# Exemplo do personagem pegando a maça com IF:

# laço c no intervalo (1,10): // for c in range(1,10):
#   SE moeda                 //     if moeda == True:
#     pegar moeda           //        print('pegar moeda')
#   passo                  //     print('Passo..')
#   pular                 //      print('Pular')
# Pega maca              //   print('Pegar')

# // Veja que o pega está fora do laço de repetição, ou seja, ele vai repetir 10 passos, sair do laço e pegar.

#### Teste 1 - Laço para pegar a maçã ####

"""
for c in range(1, 10):
    print('Passo..')
print('Pegar Maça!!')"""

#### Teste 2 - Laço para pegar a maçã ####

"""
for c in range(1, 3):
    print('Passo..')
    print('Pulo..')
print('Passo..')
print('Pegar Maça!!')"""

#### Teste 3 - Laço para pegar a maçã ####

"""
moeda = 'moeda'
Bloco = 'Bloco'
maca = 'Maça'
buraco = 'buraco'

lista = ['Bloco', 'buraco', 'moeda', 'Bloco', 'buraco', 'Bloco', 'buraco', 'moeda', 'Maça']
"""
"""
for c in range(0, 9):
    if Bloco == lista[c]:
        print('Passo..')
    if buraco == lista[c]:
        print('Pulo..')
    if moeda == lista[c]:
        print('Pegar Moeda!!')
print('Passo..')
print('Pegar Maça!!')
"""

### Aula Pratica ###

"""
for c in range(0, 6): # Cuidado para você fazer 6 vezes você deve colocar: (0, 6) é nao (1, 6) // O zero conta também.
    print('Oi')
print('Fim\n')          # Tudo que for fora do laço tem que estar na mesma linha que ele.

# Caso queira repetir o numero da lista

for c in range(1, 7): # Sua variavel de for ( No caso C), pode ser trocado por qualquer coisa. 1 ate 7 vai contar até 6.
    print(c) # Caso informe a sua variavel lah em cima ( No caso C), ele conta o seu range.
print('Fim\n')

for c in range(6, 0, -1): # (Numero inicial, Numero final, intervalo).Com -1 se conta do maior ao menor.
    print(c)
print('Fim\n')

for c in range(0, 6, 2): # Intervalo de 2 em 2.
    print(c)
print('Fim\n')"""

# inserir os valores de inicio, fim e intervalo
"""
i = int(input('Digite o inicial: '))
f = int(input('Digite o número inicial: '))
p = int(input('Digite o intervalo: '))
for c in range(i, f + 1, p): # (inicio, fim + 1, Intervalo)
    print(c)
print('FIM\n')"""

# Somar valores dentro do for.

s = 0
for teste in range(0, 3):
    n = int(input('Digite um número: ')) # ele irá pedir o valor diversas vezes.
    s += n # S receberá todos os valores de n
print('Soma dos valores foi {}!\n'.format(s))