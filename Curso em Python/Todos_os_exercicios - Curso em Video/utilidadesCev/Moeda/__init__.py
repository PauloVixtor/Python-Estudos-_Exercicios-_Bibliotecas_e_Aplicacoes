def metade(n, v=False):
    met = n/2
    if v == False:
        return met
    else:
        return f'R$ {met:.2f}'


def dobro(n, v=False):
    dob = n * 2
    if v == False:
        return dob
    else:
        return f'R$ {dob:.2f}'


def aumentar(n, q, v=False):
    aum = (n * (q/100)) + n
    if v == False:
        return aum
    else:
        return f'R$ {aum:.2f}'


def diminuir(n, q, v=False):
    dim = n - (n * (q/100))
    if v == False:
        return dim
    else:
        return f'R$ {dim:.2f}'


def moeda(n):
        return f'R$ {n:.2f}'


def resume(n, a, d):
    met = n / 2
    dob = n * 2
    aum = (n * (a / 100)) + n
    dim = n - (n * (d / 100))
    frase = 'Resumo do valor'
    return print(f'{"-" * (len(frase) + 16)}\n'
                f'        {frase}\n'
                f'{"-" * (len(frase) + 16)}\n'
                f' Preço analisado: {"":>1} R$ {n:.2f}\n'.replace('.', ','),
                f'Dobro do Preço: {"":>2} R$ {dob:.2f}\n'.replace('.', ','),
                f'Metade do Preço: {"":>1} R$ {met:.2f}\n'.replace('.', ','),
                f'{a}% de aumento: {"":>2} R$ {aum:.2f}\n'.replace('.', ','),
                f'{d}% de redução: {"":>2} R$ {dim:.2f}\n'.replace('.', ','),
                f'{"-" * (len(frase) + 16)}')