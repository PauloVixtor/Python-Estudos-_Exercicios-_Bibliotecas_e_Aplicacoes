## Operações aritmeticas ##

# Ordem de precêdencia

# 1 : resolver os ()
# 2 : resolver os ** potencia
# 3 : resolver os * mutiplicação / Divisão // Divisão inteira % resto
# 4 : resolver os + adição - subtratção

# Coisas importantes apra desenvolver #
# pow () = a potencia
# 81**(1/2). 90**(1/3) = para calcular a raiz
# 'algo escrito'*2 = a multiplicar varias vezes algo escrito
# Para centralizar algo  {:^6} / Para esquerda  {:<10} / Para direita  {:>16}
# Para centralizar é adicionar algo {:=^8} / Para o calculo ter apenas 2 casas {:.2f}
# Para não ter quebra de linha de um print para outro  , end='digite algo' / Para quebrar a linha  /n

# Exemplos de mutiplicação de algo escrito
# n = input('Escreva algo: ')
# print(n*5)
# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:=^20} !'.format(nome))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
su = n1 - n2
print('A soma é igual à {}, \n a multiplicação é igual à {},\n a divisão e igual à {:.2f} !! '.format(s, m, d), end=' ')
print(', a potencia e igual {},\n divisão inteira é igual à {}, A subtração é igual à {} !! '.format(p, di, su))


