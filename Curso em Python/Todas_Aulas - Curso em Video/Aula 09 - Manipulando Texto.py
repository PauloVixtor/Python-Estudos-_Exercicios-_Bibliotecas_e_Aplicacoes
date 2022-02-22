###### MANIPULAÇÃO DE TEXTO #######

# ----Parte Teorica----#

frase = ('Curso de video python')

# ---- Tecnica de Fatiamento -----#
# Exemplo:

print(frase[9])
# explicação: o python separa os dados por posição do texto que inicia em 0 até fim da frase.


print(frase[3:19])
# explicação: Ele vai pegar a posição inicia e final informado.
# Observação: a frase sempre começa com 0 então sempre coloque proximo número caso a frase não fique compelta.


print(frase[9:21:2])
# explicação: ao colocar o 2 no ultimo campo, contamos de duas em duas posições.

print(frase[:5])
# explicação: Ele mostra tudo que está antes da posição informada.

print(frase[15:])
# explicação: Ele mostra tudo que está depois da posição informada.

print(frase[9::3])
# explicação: Ele mostra tudo que está depois da posição informada de três em três posições.

# ---- Tecnica de Analise ----- #

print(len(frase))
# explicação: contar o comprimento ou quantidade de posições na frase.
# Observação: IMPORANTE NO CURSO.

print(frase.count('o'))
# explicação: contar a quantidade de vezes que a letra tem na frase ou quantidade de palavras e frases.

print(frase.count('o', 0, 13))
# explicação: contar a quantidade de vezes que letra o apareceu na posição inicial e final informada.

print(frase.find('deo'))
# explicação: mostra o momento em que a frase informada começou.

print(frase.find('Android'))
# explicação: mostra -1 porque a frase não existe no texto, por isso, não existe na frase.

print('Curso' in frase)
# explicação: faz uma verificação de verdadeiro ou falso, para ver se a frase informada existe no texto.
# Observação:Isso é um operador.

# ---- Tecnica de Transformação ----- #

print(frase.replace('python', 'Android'))
# explicação: ele transforma uma palavra da frase por outra.

print(frase.upper())
# explicação: ele transforma as letras em maiusculas.
# Observação: Isso é um metodo, IMPORTANTE!!!

print(frase.lower())
# explicação: ele transforma as letras em minusculas.

print(frase.capitalize())
# explicação: Ele transforma a priemira letra da frase em maiuscula.

print(frase.title())
# explicação: Ele transforma os inicios de palavra em maiusculas.

## Mudando frase ##

frase2 = ('   Aprenda python   ')

print(frase2.strip())
# explicação: Remove espaços do começo e final da frase.

print(frase2.rstrip())
# explicação: usando o R retira os espaços a direita.
# Observação: IMPORTANTE!!

print(frase2.lstrip())
# explicação: usando o L retira os espaços a esquerda.
# Observação: IMPORTANTE!!

# ---- Tecnica de Divisão ----- #

print(frase.split())
# explicação: separa os dados, nesse caso divisão por espaço( gerando novas listas).
# Observação: Estudar Bastante.

# ---- Tecnica de Junção ----- #

print('-'.join(frase))
# explicação: faz a junção dos dados, e pode adicionar uma informação sobre as letras.

sep = frase.split()
print('-'.join(sep))
## Exemplo de separação e junção diferente.





# --------- Pratica da aula 09 -------- #

frase = 'Curso em Video Python'
print(frase)

# fatiamento
print(frase[3])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])

# print("""O cantor e compositor Anthony Kiedis, do Red Hot Chili Peppers, tem mais um hit em suas mãos. Mas, desta vez, não é um single, nem o tão aguardado 12º álbum de estúdio da banda de rock: é uma casa personalizada que o vocalista construiu ao longo do litoral norte da ilha havaiana de Kauai, onde trechos de areia espalhada por pedras dão lugar a vistas deslumbrantes do oceano.""")

print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Em Java'))
print(frase[0])
java = frase.replace('Python', 'Em Java')
print(java)

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Video'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

