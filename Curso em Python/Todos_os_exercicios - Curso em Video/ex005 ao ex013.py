# Exercicio 5 - sucessor e antecessor && Correto :) &&

# n1 = int(input('Digite um número: '))
# su = n1 + 1
# an = n1 - 1
# print('Analisando o numero {}, Numero antecessor {} e o numero sucessor {} !!'.format(n1, an, su))

# Correção questão 5 a segunda forma de se fazer a atividade

# n1 = int(input('Digite um número: '))
# print('Analisando o numero {}, Numero antecessor {} e o numero sucessor {} !!'.format(n1, (n1-1), (n1+1)))

# Exercicio 6 - dobro, triplo e raiz && Correto :) &&

# n1 = int(input('Digite um valor: '))
# do = n1 * 2
# tri = n1 * 3
# raiz = n1**(1/2)
#print('O número é {},\n o dobro é {},\n o trplo é {}, \n raiz é igual {:.2f}'.format(n1, do, tri, raiz))

# Correção da questão 6 a segunda forma de fazer a atividade

# n = int(input('Digite um número: '))
# print('O número é {}, o seu dobro é igual à {} !!'.format(n, (n*2)))
# print('O número é {}, o seu triplo é igual à {} !! \nO número é {}, a sua raiz é igual à {:.2f} !!'.format(n, (n*3), n, pow(n, 1/2)))

# Exercicio 7 - nome e nota do aluno && Correto :) &&

# nome = str(input('Digite seu nome: '))
# p1 = float(input('Digite a priemira nota: '))
# p2 = float(input('Digite a segunda nota: '))
# fin = (p1+p2)/2
# print('Prazer aluno {}!! \n A média da sua nota é igual {:.1f} :'.format(nome, fin))

# Exercicio 8 - metro, centimetros e milimetros && quase :| &&

# m = float(input('Digite o valor em metros: '))
# dm = m*10
# c = m*100
# mi = m*1000
# dam = m/10
# hm = m/100
# km = m/1000
# print('Os metros são {} !\nDm e igual à {:.0f} dm !\nOs centimetros {:.0f} cm !\nOs milimetros {:.0f} mm !'.format(m, dm, c, mi))
# print('Os dam são {:.1f} dam,\nOS hm são {:.2f} hm !,\nOs quilometros {:.3f} km ! '.format(dam, hm, km))

# Exercicio 9 - tabuada && correto :) &&

# n1 = int(input('Digite um valor: '))
# x1 = n1*1
# x2 = n1*2
# x3 = n1*3
# x4 = n1*4
# x5 = n1*5
# x6 = n1*6
# x7 = n1*7
# x8 = n1*8
# x9 = n1*9
# x10 = n1*10
# print('Tabuada: |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}|'.format(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))

# Correção da questão 9 é a segunda forma de fazer

# n = int(input('Digite um número apra saber a tabuada: '))
# print('-'*12)
# print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {} '.format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5))
# print('{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {} '.format(n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
# print('-'*12)


# Exercicio 10 - valor do dolar & correto :) &&

# n1 = float(input('Digita o valor que tem na carteira: R$ '))
# d = n1 / 5.72
# e = n1 / 6.64
# l = n1 / 7.73
# print('Você tem R${:.2f} reais, você pode comprar US${:.2f} dolares !!'.format(n1, d))
# print('Você tem R${:.2f} reais, você pode comprar ${:.2f} Euros !!'.format(n1, e))
# print('Você tem R${:.2f} reais, você pode comprar ${:.2f} Libras !!'.format(n1, l))

# Exercicio 11 - calculo das paredes e tinta && Correto :) &&

# la = float(input('Digite a largura em metros: '))
# al = float(input('Digite a altura em metros: '))
# m = la*al
# t = m/2
# print('Os metros quadrados são {} m2, serão usados {:.2f} latas !!'.format(m, t))

# Correção como fazer de uma segunda forma

# la = float(input('Digite a largura em metros: '))
# al = float(input('Digite a altura em metros: '))
# m = la*al
# t = m/2
# print(' Essa parede tem dimensão {} x {} Os metros quadrados são {} m2, serão usados {:.2f} latas !!'.format(la, al, m, t))

# Exercicio 12 - Preço com desconto de 5% && Correto :) &&

# v1 = float(input('Digite um preço: '))
# des = (5/100) * v1
# v2 = v1 - des
# print('O preço de R${:.2f} por R${:.2f} !!'.format(v1, v2))

# correção segunda forma de resolver

# v1 = float(input('Digite um preço: '))
# v2 = v1 -  (5/100 * v1)
# print('O preço de R${:.2f} por R${:.2f} !!'.format(v1, v2))

# Exercicio 13 - aumento de salario de 15% && correto &&

# sa = float(input('Digite o seu salario: '))
# au = sa + (15/100 * sa)
# print('O seu salario era de R${:.2f}, com aumento de 15% seu salario irá para R${:.2f} .'.format(sa, au))

# Exercicio Extra

# pro = float(input('Digite o valor do produto: R$ '))
# des = pro - (10/100 * pro)
# par = (8/100 * pro) + pro
# print(' O valor é {},\n Se o valor for pago a vista o preço tem desconto de R$ {:.2f}. \n Quando o valor for parcelado o preço é R$ {:.2f} .'.format(pro, des, par))

