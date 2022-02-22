def leiastr(msg):
    while True:
        try:
            n = str(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número valido.\033[m')
        else:
            break
    return n


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro! Digite um número valido.\033[m')
        else:
            break
    return n
