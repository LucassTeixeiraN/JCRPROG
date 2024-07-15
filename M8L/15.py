'''Escreva um programa com uma função para receber do usuário um conjunto de
valores reais e também com funções próprias que recebem como argumento uma
lista e calculem e retornem a média, o maior, o menor e a soma dos elementos da
lista'''

def main():
    lista = criarLista()
    
    media(lista)
    maiorN(lista)
    menorN(lista)
    somaLista(lista)


def criarLista():
    lista = []

    print("Insira valores reais para compor uma lista. (Deixe em branco caso não deseje adicionar mais valores)")
    while True:
        valor = input()

        if valor == "":
            break
        
        if not valor.isalpha():
            lista.append(float(valor))
    return lista


def media(list):
    media = sum(list)/len(list)
    print(f"A média dos valores da lista é {media}")


def maiorN(list):
    maior_n = 0

    for i in list:
        if i > maior_n:
            maior_n = i

    print(f"O maior valor da lista é {maior_n}")


def menorN(list):
    menor_n = 0

    for i in list:
        if i < menor_n or menor_n == 0:
            menor_n = i

    print(f"O menor valor da lista é {menor_n}")


def somaLista(list):
    soma = sum(list)

    print(f"A soma dos elementos da lista é {soma}")

main()