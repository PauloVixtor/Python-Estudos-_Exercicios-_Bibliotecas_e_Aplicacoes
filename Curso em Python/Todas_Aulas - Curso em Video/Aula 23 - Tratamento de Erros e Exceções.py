### Aula 23 - Tratamento de Erros e Exceções ###

# Tratamento de Erros e Exceções:

# Correção de falhas do codigo.
# Não corrige erro de sintaxe, porém erros de funcionamento ele tentará corrigir.
# Faz a correção de erros semanticos.
# Existem milhares de excecoes.
# Um Try tem varios Exception

# Try: = Tente fazer algo
    # Comando que provalmente dariam problema
# Except = Exceção.
    # Caso falhe.

### Teorica ###


# Ex: Funcionando e dando erro(não entendeu a letra)

# NameErro

"""
# Erro:

print(x)

# Funcionando:
x = 8
print(x)
"""

# print(x) = X não existe no primeiro caso.

# Ex2: Erro de valor

# invalid literal for int() with base 10: 'oito'

"""
n = int(input('Número: '))
print(f'Você digitou o número {n}')
"""

# Caso você digite o numero 8 por extenso "oito", o programa irá dar erro.


# Ex3: Erro de divisão

# Division by zero

"""
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
r = a/b
print(f'O resultado é {r}')
"""

# Erro de divisão por 0, que não existe.

# Ex4: Erro em diferentes tipos primitivos

# TypeError

"""
a = 5
b = '5'
r = a/b
print(r)
"""

# Caso de erro por um ser considerado numero e ouro texto.

# Ex5: Erro com listas

# IndexErro

"""
lst = [3, 6, 4]
print(lst[3])
"""

# Lista começa em zero, por isso

# Ex6: Erro na importação

# ModuleNotFoundError
"""
import x
"""

# Quando uma importação não existe

### Pratica ###

# Usando Try, Execpt, Else e Finally:

"""
# Tente
try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    r = a/b
# Caso apareça o erro
except:
    print('Infelizmente tivemos um probelma! :(')
# Caso tenha funcionado
else:
    print(f'O resultado é {r:.1f}')
# Funciona independente de erro ou funcionar sempre vai acontecer.(Ex: fechar o banco, Drive selenium e etc).
finally:
    print('Volte Sempre')
"""

# Except Exception as erro = Cria a variavel erro.

"""
# Operação
try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    r = a/b
# Falhou
except Exception as erro:
    print(f'Problema encontra foi "{erro.__class__}"')
# Deu certo
else:
    print(f'O resultado é {r:.1f}')
# Certo/ Falha
finally:
    print('Volte Sempre')"""

# Varios Exception: Varios tipos de erro(TypeError, ValueError, ZeroDivisionError,

"""
# Operação
try:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    r = a/b
# Falhou
except (TypeError, ValueError):
    print(f'Tivemos problemas com os tipos de dados que você digitou!"')
except ZeroDivisionError as zero:
    print(f'Não é possivel dividir por Zero!')
except KeyboardInterrupt:
    print('O Usuario preferiu não informar dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
# Deu certo
else:
    print(f'O resultado é {r:.1f}')
# Certo/ Falha
finally:
    print('Volte Sempre')"""
