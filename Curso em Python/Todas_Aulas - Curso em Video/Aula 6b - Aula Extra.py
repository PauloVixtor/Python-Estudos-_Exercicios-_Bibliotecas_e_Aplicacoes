# Os tipos primitivos int(valor), float(valor flutuante 1.0), bool (vdd ou falso) e str(qualquer caractere)
#n = bool(input('Digite o valor:'))
#print(n)

##### TUDO QUE TIVER .IS***** É UMA VERIFICAÇÃO ######

# Como saber se algo e um numero
#n = (input('Digite algo:'))
#print(n.isnumeric())

# Como saber se é uma letra do alfabeto
#n = (input('Digite algo:'))
#print(n.isalpha())

# Comos saber se é um numero e letra
#n = (input('Digite algo:'))
#print(n.isalnum())

# Como saber se somente tem letras maiusculas
#n = (input('Digite algo:'))
#print(n.isupper())

##   Desafio 1 da aula 6  ##

#nu1 = int(input('Digite um valor?: '))
#nu2 = int(input('Digite outro valor?: '))
#nu3 = int(input('Digite outro valor?: '))
#soma = nu1 + nu2 + nu3
#print('O valor da soma de {} + {} + {} é igual à {}'.format(nu1, nu2, nu3, soma))

### Os tipos de primtivos
#n1 = int(input('Digite um numero: '))
#n2 = str(input('Digite algo: '))
#n3 = bool(input('Digite algo: '))
#n4 = float(input('Digite numero de porcentagem: '))
#print(type(n1))
#print(type(n2))
#print(type(n3))
#print(type(n4))

## Qual o tipo de dado que está sendo inserido ##
n = input('Digite algo: ')
print('O tipo primitivo desse exercicio e:', type(n))
print(' é um numero e letra? ', n.isalnum())
print('E um decimal? ', n.isdecimal())
print('E um numero? ', n.isnumeric())
print('E uma letra? ', n.isalpha())
print('E maiusculo? ', n.isupper())
print('E minusculo? ', n.islower())
print('Só tem espaços nele? ', n.isspace())
print('Está capitalizada? ', n.istitle())


