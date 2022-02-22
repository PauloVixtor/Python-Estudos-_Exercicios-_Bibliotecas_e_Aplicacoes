from hashlib import sha256
import time

def aplicar_256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(num_bloco, transacoes, hash_anterior, gtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_256(texto)
        if meu_hash.startswith("0" * gtde_zeros):
            return nonce, meu_hash
        nonce += 1
if __name__ == "__main__":
    num_bloco = 15
    transacoes = """
    Lira->Alon->10
    Alon->Joao->5
    Joao->Amanda->11
    """
    gtde_zeros = 7
    hash_anterior = "abc"
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, gtde_zeros)
    print(resultado)
    print('{:.2f}'.format(time.time() - inicio))

""""print(sha256("abc".encode("ascii")).hexdigest())
# Para codificar no sha256.( Resultado mostra objeto) // Para ver o hash"""
