### Aula 19 - Dicionários ###

# Dicionarios servem para nomear indices de uma lista, tornando mais facil na hora de especificar o valor desejado.
# Substituindo numeros por nomes, ou int por str.


### Identificadores ###

# Tuplas() = podem ou não usar parenteses.
# Listas[]
# Dicionários{}


#### Teoria ####

## Como criar um dicionario ##

# Dados = dict() // Cria Dicionário.
# Dados = {}    // Também cria dicionário.

## Adicionando dados ##

# Tabela = Dados
# Coluna = Nome, Idade
# Registros = Pedro, 25
"""
Dados = {'Nome': 'Pedro', 'Idade': 25}
print(Dados['Nome'])
print(Dados['Idade'])"""

## Adicionar novo indice(coluna) ##

# Dados['Sexo'] = 'M'
# print(Dados)

## Deletar indice(coluna) ##

# del Dados['Idade']
# print(Dados)

## Novo Exemplo ##

"""
filmes = {
    'Titulo': 'Star Wars',
    'Ano': 1997,
    'Diretor': 'George Lucas'
}
print(filmes)"""

## Itens, Chaves, Valores ##

# print(filmes.values()) # Ver valores ( Registros).
# print(filmes.keys()) # Ver chaves ( colunas).
# print(filmes.items()) # Ver Itens ( colunas + registros em tuplas).

## Usando o FOR em um dicionario ##

"""
print('\n')
for k, v in filmes.items():
    print(f'O {k} é {v}') # Escreve as colunas e os registros dentro do dicionario."""

## Juntando Dicionarios, listas e Tuplas ##

# Dicionario dentro de Listas:

# print('\n')
# locadora = [filmes, filmes] # adicionar dicionario em uma lista
# print(locadora)

# Listas dentro de Dicionarios:

"""
filmes2 = {
    'Titulo': ['Star Wars', 'Avangers', 'Matrix'],
    'Ano': [1997, 2012, 1999],
    'Diretor': ['George Lucas', 'Joss Whendon', 'Wachowski']
}
print(filmes2)"""

## Escolher dados especificos ##

# print(locadora[0]['Ano']) # Irá mostrar o ano do indice 0
# print(locadora[2]['Titulo']) # Vai mostrar o indice 2 do titulo


#### Pratica ####

## Mostrando Dicionario ##

pessoas = {
    'nome': 'Gustavo',
    'idade': '22',
    'sexo': 'M'
}
# print(pessoas)


## Mostrar nome ( coluna especifica) ##
# print(pessoas['nome']) # Mostra Gustavo
# print(pessoas['idade']) # Mostra 22


## Mostrando separado ##
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # Para mostrar dentro de aspas '' deve se usar "".


## Mostrar colunas ##
# print(pessoas.keys()) # Todas colunas.


## Mostrar registros ##
# print(pessoas.values()) # todos valores.


## Mostrar Registros e Colunas ##
# print(pessoas.items()) # Colunas + Registros.


## Mostrar Dicionario usando Laço For ##

"""
for k in pessoas.keys():
    print(k) # Mostra todas Colunas
print('\n')
for v in pessoas.values():
    print(v) # Mostra todos Registros
print('\n')
for k, v in pessoas.items():
    print(f'{k} = {v}') # Mostra todos Registros e colunas formatados"""

## Apagando colunas ##
# del pessoas['sexo'] # Apaga a coluna sexo
# print(pessoas)


## Alterar dados ##
# pessoas['nome'] = 'Leandro'
# print(pessoas) # Altera o nome de Gustavo para Leandro


## Criando nova coluna e inserindo registro
# pessoas['peso'] = 98.5
# print(pessoas)


## Dicionarios dentro de listas ##
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro','Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo','Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)"""

# print(estado1) # mostra dicionario do estado do RJ
# print(estado2) # mostra dicionario do estado do SP
# print('\n')
# print(brasil) #Mostra a lista Brasil


## Mostrando um dicionario dentro da lista ##
# print(brasil[1]) # mostra dicionario do estado do SP na lista

## Mostrando o valor de uma coluna do dicionario ##
# print(brasil[0]['uf']) # Mostra o RJ
# print(brasil[0]['Sigla']) # Sigla do RJ

## Mostrando funcionalidade da lista em dicionario ##
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')) # como adicionar os dados diretamente ao dicionario
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # IMPORTANTE fazer a copia dos dados.
print(brasil) # Resultado correto
print('\n')

## Dentro da lista para dicionario com laço ##
for e in brasil: # For da lista
    for k, v in e.items(): # For do dicionario
        print(f'O campo {k} tem valor {v}') # Mostrando por valores do dicionario
        
for e in brasil: # mostra lista
    for v in e.values(): # mostra valor do dicionario
        print(v, end=' ')
    print()"""

