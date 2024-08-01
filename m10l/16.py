# Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve o número de listas em w ordenadas por ordem
# crescente em sentido lato, ou seja, em que cada elemento é menor ou igual que o
# seguinte. Por exemplo, no caso da lista [[2,2,3,0],[1,2,5,4],[2,4,4]] a função deve
# devolver 1 pois só a terceira lista está ordenada.

def listaCrescente(lista):

    if len(lista) <= 1:
        return True  
    return lista[0] <= lista[1] and listaCrescente(lista[1:])

def contagemDeListas(lista):

    if not lista:
        return 0
    elif listaCrescente(lista[0]):
        return 1 + contagemDeListas(lista[1:])  
    else:
        return contagemDeListas(lista[1:]) 


def main():
    while True:
        try:
            w = []
            n_listas = int(input("Insira o número de listas dentro da lista: "))
            print("Insira as listas deixando espaço entre os elementos e pressionando ENTER entre cada lista")
            for i in range(n_listas):
                lista = [int(num) for num in input().split()]
                w.append(lista)
            print(f"{contagemDeListas(w)} listas está(ão) ordenada(s)")
            break
        except ValueError:
            print("Valor inválido")
main()