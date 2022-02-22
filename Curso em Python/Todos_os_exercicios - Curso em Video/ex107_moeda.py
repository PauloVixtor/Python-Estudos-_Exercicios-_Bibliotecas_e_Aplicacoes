def metade(n):
    met = n/2
    return met


def dobro(n):
    dob = n * 2
    return dob


def aumentar(n, taxa):
    aum = (n * taxa/100) + n
    return aum


def diminuir(n, taxa):
    dim = n - (n * taxa/100)
    return dim

def moeda(n):
        return f'R$ {n:.2f}'

def juros_compostos(valor, taxa_ano, mensal, tempo):
    for c in range(1, tempo * 12 + 1):
        taxa = (valor * ((taxa_ano/100)/12))
        valor += taxa + mensal
    return valor