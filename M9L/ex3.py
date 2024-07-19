'''Escreva uma função que imprime, linha a linha, os valores de uma matriz
bidimensional dada como argumento.
'''
def Matriz():
    linhas = int(input("Insira a quantidade de linhas da matriz: "))
    colunas = int(input("Insira a quantidade de colunas da matriz: "))
   
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f"Insira um valor numerico inteiro para {i,j}: ")))
        matriz.append(linha)
    print("Matriz = ", matriz)

Matriz()