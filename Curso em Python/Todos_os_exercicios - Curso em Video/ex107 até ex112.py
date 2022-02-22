### Desafio 107 ### - Correto

# Crie o modelo moeda.py
# que tenha as funções incorporadas aumentar(), Diminuir(), Dobro(), metade().

# Faça também um programa que importa essas funções e use algumas dessas funções.

"""
import ex107_moeda

num = float(input('Digite o valor R$: '))
taxa = float(input('Digite a taxa: '))
print(f'O dobro de R${num} e R${ex107_moeda.dobro(num):.2f}')
print(f'A metade de R${num} e R${ex107_moeda.metade(num):.2f}')
print(f'Aumentar 10%, temos R${ex107_moeda.aumentar(num, taxa):.2f}')
print(f'Diminuir 13%, temos R${ex107_moeda.diminuir(num, taxa):.2f}')"""

# ideia
"""
import ex107_moeda

v = float(input('Digite o valor R$: '))
t = float(input('Digite a taxa anual: '))
m = float(input('Digite o valor mensal R$: '))
temp = int(input('Digite a quantidade de anos: '))
print(f'O valor de retorno do inv estimento é {ex107_moeda.juros_compostos(v, t, m, temp):.2f}')"""



### Desafio 108 ### - Revisão

# Adapte o codigo 107
# Criando uma função adicional chamada moeda() que consiga mostrar o valor monetario formatado

"""
import ex108_moeda

num = float(input('Digite o valor R$: '))
print(f'O dobro de {ex108_moeda.moeda(num)} e {ex108_moeda.moeda(ex108_moeda.dobro(num))}')
print(f'A metade de {ex108_moeda.moeda(num)} e {ex108_moeda.moeda(ex108_moeda.metade(num))}')
print(f'Aumentar 10%, temos {ex108_moeda.moeda(ex108_moeda.aumentar(num))}')
print(f'Diminuir 13%, temos {ex108_moeda.moeda(ex108_moeda.diminuir(num))}')
"""

### Desafio 109 ### - Correto

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais
# Informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# Desenvolvida no desafio 108


"""
import ex109_moeda

num = float(input('Digite o valor R$: '))
print(f'O dobro de {ex109_moeda.moeda(num)} e {ex109_moeda.dobro(num, True)}')
print(f'A metade de {ex109_moeda.moeda(num)} e {ex109_moeda.metade(num, False)}')
print(f'Aumentar 10%, temos {ex109_moeda.aumentar(num, 10, True)}')
print(f'Diminuir 13%, temos {ex109_moeda.diminuir(num, 13, True)}')"""



### Desafio 110 ### - Correto

# Adicione ao modelo moeda.py a função chamada Resumo()
# Que mostra na tela algumas informações geradas pelas funções que já temos no modelo criado até aqui.

"""
import ex110_moeda

num = float(input('Digite o preço: R$ '))
ex110_moeda.resume(num, 80, 35)"""


### Desafio 111 ### -

# Crie um pacote chamado utilidadesCev
# Que tenha dois modulos internos: moeda e dados.
# Tranfira todas as finções dos exercicios 107, 108 e 109
# E mantenha tudo funcionando

"""
from utilidadesCev import Moeda

num = float(input('Digite o preço: R$ '))
Moeda.resume(num, 80, 35)"""


### Desafio 112 ### - Revisão

# Dentro do pacotes utilidadesCev que criamos no exercicio 111, temos o modulo chamado dados
# Crie um programa que chama a função leiadinheiro() que seja capaz de funcionar como input
# Mas cim uma validação de dados monetarios

"""
from utilidadesCev import Moeda, Dado

num = Dado.leiadinheiro('Digite o preço: R$ ')
Moeda.resume(num, 80, 35)"""