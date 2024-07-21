'''Crie um programa que implemente e teste uma função que, dadas duas listas
representando dois conjuntos:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo.'''

# def uniao_conjuntos(conjunto1, conjunto2):
#     return list(set(conjunto1) | set(conjunto2))

# def intersecao_conjuntos(conjunto1, conjunto2):
#     return list(set(conjunto1) & set(conjunto2))

# def diferenca_conjuntos(conjunto1, conjunto2):
#     return list(set(conjunto1) - set(conjunto2))

# def eh_subconjunto(conjunto1, conjunto2):
#     return set(conjunto1).issubset(set(conjunto2))

def criar_conjuntos():
    print("Insira os conjuntos (use ESPAÇO entre os números)")
    numeros = input()
    while True:
        try:
            conjunto = [int(i) for i in numeros.split()]
            return conjunto
        except ValueError:
            print("Valores inválidos")


def uniao_conjuntos(conjunto1, conjunto2):
    conjuntoUniao = conjunto1.copy()
    
    for i in conjunto2:
        if not i in conjuntoUniao:
            conjuntoUniao.append(i)
        
    conjuntoUniao.sort()
    return conjuntoUniao


def intersecao_conjuntos(conjunto1, conjunto2):
    conjuntoIntersec = []

    for i in conjunto1:
        if i in conjunto2 and not i in conjuntoIntersec:
            conjuntoIntersec.append(i)

    conjuntoIntersec.sort()
    return conjuntoIntersec


def diferenca_conjuntos(conjunto1, conjunto2):
    conjuntoDif = []

    for i in conjunto1:
        if not i in conjunto2:
            conjuntoDif.append(i)
    
    conjuntoDif.sort()
    return conjuntoDif 


def eh_subconjunto(conjunto1, conjunto2):

    for i in conjunto1:
        if not i in conjunto2:
            return "Não"

    return "Sim"


def main():
    conjunto1 = criar_conjuntos()
    conjunto2 = criar_conjuntos()

    print("-"*40)
    print("União dos conjuntos:", uniao_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("Interseção dos conjuntos:", intersecao_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("Diferença entre os conjuntos (conjunto1 - conjunto2):", diferenca_conjuntos(conjunto1, conjunto2))
    print("-"*40)
    print("O primeiro conjunto é um subconjunto do segundo:", eh_subconjunto(conjunto1, conjunto2))
    print("-"*40)

main()
