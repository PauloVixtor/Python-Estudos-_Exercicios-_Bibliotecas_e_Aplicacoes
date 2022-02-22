### Aula 18 - Listas (Parte 2) ###

# Nessa aula iremos aprender mais os conceitos de lista dentro de lista.

#### Teoria ####

# Criando copia dos dados
"""
dados = ['Pedro', 25]
pessoas = list()
pessoas.append(dados[:]) # Cria a copia de uma lista
print(pessoas)"""

# Lista dentro de lista
"""
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0], pessoas[1], pessoas[2]) # Como pegar apenas as listas separadas.
print(pessoas[0][0], pessoas[1][0], pessoas[2][0]) # Apenas os nomes, ou seja, primeiro item de cada lista.
print(pessoas[0][1], pessoas[1][1], pessoas[2][1]) # Apenas a idade, ou seja, segundo item de cada lista.
"""
#### Pratica ####

# Criando a lista

"""
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

# colocando alista dentro de outro lista

galera = list()
galera.append(teste[:]) # adicionou uma copia, sempre crie uma copia
# galera.append(teste) # // forma errada de fazer
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # Crie uma copia, para aplicar a alteração"""
# print(galera)

# Criando lista dentro de lista

#### Estrutura ####


# galera = [[], [], []]


#### Dados ####

"""
galera =[['João', 19], ['Maria', 22], ['Joaquim', 13], ['Maria', 45]]
print(galera)

#### Dados João ####

# print(galera[0])

#### Apenas o nome de João ####

# print(galera[0][0])

#### FOR em uma lista composta

for p in galera:
    print(f'O nome é {p[0]}, idade {p[1]} anos!')"""

#### lista temporaria ####
"""
galera = list()
dado = list()
totmai = totmin = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    # galera.append(dado) // Caso deixe ele assim ligado, ao apagar ele tbm apagará a lista galera.
    dado.clear()
print(galera) # adicionado as listas em uma nova lista.

#### Apenas mostrar pessoas com mais de 210 anos ####

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmin += 1"""
# print(f'Temos {totmai} maior(es) de idade e {totmin} menor(es) de idade!')
