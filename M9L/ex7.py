'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
diagonal.'''

def matrizDiagonal(matriz):
   
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if i != j and matriz[i][j] != 0:
                return False
    return True
# Matriz diagonal
matriz1 = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]
# Matriz nao diagonal
matriz2 = [
    [1, 0, 1],
    [0, 2, 0],
    [0, 0, 3]
]

print(matrizDiagonal(matriz1))  # Deve retornar True
print(matrizDiagonal(matriz2))  # Deve retornar False

# main
# input das matrizes
