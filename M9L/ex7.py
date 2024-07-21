'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
diagonal.'''

def lerMatriz():
    lista = []  # Cria uma lista vazia para armazenar as linhas da matriz

    # Solicita ao usuário que insira a matriz, linha por linha
    print("Insira uma lista bidimensional colocando espaços entre os elementos de uma linha e apertando ENTER entre cada linha")
    print("Obs: Deixe a linha vazia quando não houver mais elementos a serem lidos")
    while True:
        try:
            linha = input()  # Lê uma linha da entrada
            if linha == "":
                break  # Se a linha estiver vazia, encerra a leitura
            valor = [int(numero) for numero in linha.split()]  # Converte os números da linha para inteiros

            lista.append(valor)  # Adiciona a linha à lista
        except ValueError:
            print("Valor inválido")  # Trata exceções caso o usuário insira um valor não inteiro
            
    return lista

def mostrarMatriz(matriz):
    print("-" * 60)
    for i in matriz:
        print(i)  # Imprime cada linha da matriz
    print()

def matrizDiagonal(matriz):
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if i != j and matriz[i][j] != 0:
                return False  # Se encontrar um elemento diferente de zero fora da diagonal, retorna False
    return True  # Se não encontrar nenhum elemento diferente de zero fora da diagonal, retorna True

def main():
    matriz = lerMatriz()  # Lê a matriz do usuário

    mostrarMatriz(matriz)  # Mostra a matriz na tela
    if matrizDiagonal(matriz):
        print("A matriz é diagonal")
    else:
        print("A matriz não é diagonal")
    print("-" * 60)

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
