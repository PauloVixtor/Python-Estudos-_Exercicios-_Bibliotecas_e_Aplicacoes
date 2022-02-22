def metade(n, v=False):
    met = n/2
    if v == False:
        return met
    else:
        return f'R$ {met:.2f}'.replace('.', ',')


def dobro(n, v=False):
    dob = n * 2
    if v == False:
        return dob
    else:
        return f'R$ {dob:.2f}'.replace('.', ',')


def aumentar(n, q, v=False):
    aum = (n * (q/100)) + n
    if v == False:
        return aum
    else:
        return f'R$ {aum:.2f}'.replace('.', ',')


def diminuir(n, q, v=False):
    dim = n - (n * (q/100))
    if v == False:
        return dim
    else:
        return f'R$ {dim:.2f}'.replace('.', ',')

def moeda(n):
        return f'R$ {n:.2f}'.replace('.', ',')