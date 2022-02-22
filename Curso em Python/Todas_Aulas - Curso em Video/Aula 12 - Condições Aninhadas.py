### Aula 12 - Condições Aninhadas ###

### Aula Teorica ###

# Conceito - Essa aula explica que os codigos podem ter varios caminhos, não somente verdadeiro ou falso.

# Dessa forma utilizamos "else" para fazer mais caminhos.

# IF = Se isso acontecer faça isso.
# ELIF = Em caso do IF não acontecer, use outro caminho. (Esse codigo serve como ELSE, porém ele fica simplificado).
# ELSE = Em caso do IF não acontecer, use esse caminho.

### Estrutura de condições alinhadas ###

# if carro.esquerda():
# bloco de informações do caminho usado.

# elif carro.direita(): (obs: Você pode usar diversas vezes, quantas vezes for necessario.)
# bloco de informações do caminho usado.

# else carro.direita(): (Pode ser usado uma vez, ou nem uma dependendo do codigo.)
# bloco de informações do caminho usado.

### Aula Pratica ###

nome = str(input('Digite seu nome: ')).strip().title()
if nome == 'Paulo':
    print(f'Que nom legal você tem {nome}!!')
    print(f'Tenha um bom dia, {nome}!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Gustavo':
    print('Seu nome é bem popular no brasil!!')
    print(f'Tenha um bom dia, {nome}!!')
elif nome in 'Ana Claudia Maria Jessica Juliana':
    print('Esse nome feminino e lindo!!')
    print(f'Tenha um bom dia, {nome}!!')
else:
    print(f'Seu nome é bem normal!!')
    print(f'Tenha um bom dia, {nome}!!')

# Obs: o "elif" pode ser usado diversas vezes, o "else" é opcional.
