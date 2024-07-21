'''Crie um programa que implemente e teste uma função que, dadas duas listas
representando dois conjuntos:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo.'''

# Cria os conjuntos
def criar_conjuntos():
    print("Insira os conjuntos (use ESPAÇO entre os números e ENTER ao final do conjunto)")
    numeros = input()
    while True:
        try:
            conjunto = [int(i) for i in numeros.split()]  # Converte a entrada do usuário em uma lista de inteiros
            return conjunto
        except ValueError:
            print("Valores inválidos")  # Mensagem de erro para entradas não inteiras

# União dos conjuntos
def uniao_conjuntos(conjunto1, conjunto2):
    conjuntoUniao = conjunto1.copy()  # Cria uma cópia do primeiro conjunto
    
    for i in conjunto2:
        if not i in conjuntoUniao:  # Adiciona elementos do segundo conjunto que não estão no primeiro
            conjuntoUniao.append(i)
        
    conjuntoUniao.sort()  # Ordena a lista resultante
    return conjuntoUniao

# Interseção dos conjuntos
def intersecao_conjuntos(conjunto1, conjunto2):
    conjuntoIntersec = []

    for i in conjunto1:
        if i in conjunto2 and not i in conjuntoIntersec:  # Adiciona elementos que estão em ambos os conjuntos
            conjuntoIntersec.append(i)

    conjuntoIntersec.sort()  # Ordena a lista resultante
    return conjuntoIntersec

# Diferença entre os conjuntos
def diferenca_conjuntos(conjunto1, conjunto2):
    conjuntoDif = []

    for i in conjunto1:
        if not i in conjunto2:  # Adiciona elementos do primeiro conjunto que não estão no segundo
            conjuntoDif.append(i)
    
    conjuntoDif.sort()  # Ordena a lista resultante
    return conjuntoDif 

# Verifica se o primeiro conjunto é um subconjunto do segundo
def eh_subconjunto(conjunto1, conjunto2):
    for i in conjunto1:
        if not i in conjunto2:  # Verifica se todos os elementos do primeiro conjunto estão no segundo
            return "Não"

    return "Sim"

# Função principal para testar as operações de conjuntos
def main():
    conjunto1 = criar_conjuntos()  # Cria o primeiro conjunto
    conjunto2 = criar_conjuntos()  # Cria o segundo conjunto

    print("-"*40)
    print("União dos conjuntos:", uniao_conjuntos(conjunto1, conjunto2))  # Exibe a união dos conjuntos
    print("-"*40)
    print("Interseção dos conjuntos:", intersecao_conjuntos(conjunto1, conjunto2))  # Exibe a interseção dos conjuntos
    print("-"*40)
    print("Diferença entre os conjuntos (conjunto1 - conjunto2):", diferenca_conjuntos(conjunto1, conjunto2))  # Exibe a diferença entre os conjuntos
    print("-"*40)
    print("O primeiro conjunto é um subconjunto do segundo:", eh_subconjunto(conjunto1, conjunto2))  # Verifica se o primeiro conjunto é um subconjunto do segundo
    print("-"*40)

main()  # Chama a função principal

