###### Conceito das Condições Simples ######

# tempo = int(input('Quantos anos seu carro tem? : '))
# if tempo <= 3:
#    print('Carro Novo!!')
# else:
#    print('Carro Velho!!')
# print('--FIM!!--')

## Outra forma de Fazer ##

# print('Carro Novo!!' if tempo <=3 else 'Carro Velho!!')


############# Pratica de Condições - caso 1 ############

# nome = str(input('Qual o seu nome? :')).strip()
# if nome == 'Paulo':
#    print('Que nome lindo que você tem!!')
# explicação: ele criou uma condição que pode acontecer caso a condição seja o nome especificado, ou seja, condição simples
# else:
#    print('Que nome legal!!')
# explicação: ele cria uma segunda respota caso o nome não seja o especificado, ou seja, condição composta.
# print('Bom dia {}!!'.format(nome))

#### Caso 2 ####

n1 = float(input('Digite a primeira nota? :'))
n2 = float(input('Digite a segunda nota? :'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}!!'.format(m))
# if m >= 6.0:
#    print('A sua nota foi {}, parabéns você foi aprovado!! '.format(m))
# else:
#    print('A sua nota foi {}, estude mais!!'.format(m))
# explicação: Nesse caso a condição comparava se o valor era maior ou igual a 6 para mostrar se o aluno foi aprovado ou reprovado.
# OBs: Caso apenas tenha o IF e simples, se o codigo tiver IF e ELSE e uma condição composta.

### outra forma ####

print('Parabéns!!' if m>=6 else 'estude mais!!')
# Essa condição e simplicada no caso fizemos o mesmo procedimento em apenas uma linha.
