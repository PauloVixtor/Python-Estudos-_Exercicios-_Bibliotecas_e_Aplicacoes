### Aula 22 - Módulos e Pacotes ###

# Modularização:
# > Ato de construir modulos.
# > Surgiu nos anos 60.
# > Sistemas cada vez maiores.
# > Foco: principal e dividir programas grandes com muitas funcionaldiades.
# > Foco: Aumentar a legibilidade.
# > Foco: Facilitar a manutenção do codigo.
# > Biblioteca ou pacotes: São codigos criados e importados para facilitar o uso atraves de funções.
# > Pacotes: Uma pasta que contém modulos, classificado por assuntos.

### Teorica ###

# Ex: Criando uma pasta a parte chamada uteis com funções criadas e importando apra codigo principal.

# Forma 1º de fazer:

"""
import uteis # importando pasta da maquina

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num) # Chamando as funções
print(f'O fatorial de {num} e {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')
print(f'O triplo de {num} é {uteis.triplo(num)}.')
"""

# Forma 2º de fazer:

# CAso você importe duas funções de mesmo nome, a que vale e a ultima.

"""
from uteis import fatorial, dobro, triplo # importando funões especificas

num = int(input('Digite um valor: '))
fat = fatorial(num) # Chamando as funções
print(f'O fatorial de {num} e {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
print(f'O triplo de {num} é {triplo(num)}.')
"""

### Vantagens de usar modularização ###

# > Organização do seu codigo (ou seja, dividir o codigo em partes menores).
# > Facilitar a manutenção ( alterar a função ou mudar).
# > Ocultação de codigo detalhado.
# > Reutilizar em outros projetos (usar em diversos projetos).


### Pratica ###

# Criando um modulo e aplicando ele em um projeto

# > Como criar um modulo : clicando com botão direito > New >  Python Package > digite nome > enter.
# > Para criar o assunto: clicando com botão direito > New >  Python Package > digite nome > enter.
# > Como a pasta ModuloUteis criada.


# Como importar o modulo e o assunto do modulo.

"""
from ModuloUteis import Numeros

num = int(input('Digite um valor: '))
fat = Numeros.fatorial(num) # Chamando as funções
print(f'O fatorial de {num} e {fat}.')
print(f'O dobro de {num} é {Numeros.dobro(num)}.')
print(f'O triplo de {num} é {Numeros.triplo(num)}.')
"""
