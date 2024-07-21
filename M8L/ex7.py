'''Crie um programa que implemente e teste uma função que, dadas duas listas
representando dois conjuntos:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo.'''

def uniao_conjuntos(conjunto1, conjunto2):
    return list(set(conjunto1) | set(conjunto2))

def intersecao_conjuntos(conjunto1, conjunto2):
    return list(set(conjunto1) & set(conjunto2))

def diferenca_conjuntos(conjunto1, conjunto2):
    return list(set(conjunto1) - set(conjunto2))

def eh_subconjunto(conjunto1, conjunto2):
    return set(conjunto1).issubset(set(conjunto2))


def main():
    conjunto1 = [1, 2, 3, 4]
    conjunto2 = [3, 4, 5, 6]

    print("-"*40)
    print("União dos conjuntos:", uniao_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("Interseção dos conjuntos:", intersecao_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("Diferença entre os conjuntos (conjunto1 - conjunto2):", diferenca_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("É conjunto1 um subconjunto de conjunto2?", eh_subconjunto(conjunto1, conjunto2))
    print("-"*40)

main()
