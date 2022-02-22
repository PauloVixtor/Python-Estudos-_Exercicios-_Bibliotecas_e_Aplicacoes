### Aula 11 - Cores no Terminal ###

# Conceito ANSI(Escape Sequence) - Padrão de normalização, que serve para varioas ambientes, no nosso caso será usado em um terminal.
# Codigo Inteligente
# Para representar uma cor no python você sempre vai usar ex: \033[ STYLE, TEXT, BACKGROUND  m
# Ex: \033[0;33;44m - Use padrõa depois indique os valores de estilo, texto e cor de fundo.

# Codigos para estilo(Style) - 0(Sem estilo,caso não queria colcoar tudo bem), 1(Negrito), 4(Sublinhado), 7(Inverter). Existem outros, mais esses são os melhores.
# Cor do Texto(Text) - 30 (Preto), 31 (red), 32(green), 33 (yellow), 34 (Blue), 35 (violet), 36 (ciano), 37 (gray).
# Cor de fundo(Back) - 40 (Preto), 41 (red), 42(green), 43 (yellow), 44 (Blue), 45 (violet), 46 (ciano), 47 (gray).


### Exemplos na pratica ###

# Obs: podem ser colocados em outra ordem cor do texto e fundo.
# Padrão e Branco.
"""
\033[0;30;41m # Sem estilo, letra branca e fundo vermelho
\033[4;33;36m # Sublinhado, letra amarela e fundo ciano.
\033[1;35;43m # negrito, letra violeta e fundo amarelo.
\033[30;42m # Sem estilo, letra branca e fundo verde.
\033[m   # Sem estilo, letra cinza e fundo preto (voltar ao Padrão).
\033[7;30m   # # Inverter, cor de fundo branco.

"""

### Pratica - Cores no Terminal ###
"""
print('\033[31;40mOla, mundo!!\033[m') # Para cobrir apenas o necessario se adiciona o mesmo codigo ao final.
print('\033[4;45mOla, mundo!!\033[m')
print('\033[7;33;44mOla, mundo!!\033[m') # inverte fundo e cor.

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a,b)) # Apenas destacar as cores nos resultados.
"""
# Assinatura teste.
"""

print('=============================')
print('||\033[32mSeja Bem Vindo,\033[m          ||')
print('||\033[33m  Iremos fazer    \033[m       ||')
print('||\033[35m    Coisas Incríveis!!   \033[m||')
print('||         \033[46m=)\033[m \033[4mCerto\033[m!!      ||')
print('============================')

"""
nome = 'Paulo'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'Pretoe branco':'\033[7;30m'} # Dicionario de cores.
# print('Ola prazer em te conhecer {}{}{}!!'.format('\033[4;34m',nome,'\033[m'))

print('Ola prazer em te conhecer {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))