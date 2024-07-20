'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
diagonal.'''

def lerMatriz():
    lista = []

    print("Insira uma lista bidimensional colocando espaços entre os elementos de uma linha e apertando ENTER entre cada linha")
    print("Obs: Deixe a linha vazia quando não houver mais elementos a serem lidos")
    while True:
        try:
            linha = input()
            if linha == "":
                break
            valor = [int(numero) for numero in linha.split()]

            lista.append(valor)
        except ValueError:
            print("Valor inválido")
            
    return lista

def mostrarMatriz(matriz):
    print("-"*60)
    for i in matriz:
        print(i)
    print()

def matrizDiagonal(matriz):
   
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if i != j and matriz[i][j] != 0:
                return False
    return True

def main():
    matriz = lerMatriz()

    mostrarMatriz(matriz)
    if matrizDiagonal(matriz) == True:
        print("A matriz é diagonal")
    else:
        print("A matriz não é diagonal")
    print("-"*60)

main()


# Matriz diagonal
# matriz1 = [
#     [1, 0, 0],
#     [0, 2, 0],
#     [0, 0, 3]
# ]
# Matriz nao diagonal
# matriz2 = [
#     [1, 0, 1],
#     [0, 2, 0],
#     [0, 0, 3]
# ]
