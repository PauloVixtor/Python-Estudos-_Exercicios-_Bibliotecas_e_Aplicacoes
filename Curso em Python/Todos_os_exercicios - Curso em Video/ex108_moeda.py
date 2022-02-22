def metade(n=0):
    met = n/2
    return met


def dobro(n=0):
    dob = n * 2
    return dob


def aumentar(n=0):
    aum = (n * 0.10) + n
    return aum


def diminuir(n=0):
    dim = n - (n * 0.13)
    return dim


def moeda(n=0):
        return f'R$ {n:.2f}'.replace('.', ',')