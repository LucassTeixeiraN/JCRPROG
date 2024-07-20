'''Escreva uma função que imprime, linha a linha, os valores de uma matriz
bidimensional dada como argumento.
'''
def criarMatriz():
    while True:
        try:
            linhas = int(input("Insira a quantidade de linhas da matriz: "))
            colunas = int(input("Insira a quantidade de colunas da matriz: "))
            matriz = []
            for i in range(linhas):
                linha = []
                for j in range(colunas):
                    while True:
                        try:
                            linha.append(int(input(f"Insira um valor numerico inteiro para {i+1,j+1}: ")))
                            break
                        except ValueError:
                            print("Valor Inválido")
                matriz.append(linha)
            return matriz
        except ValueError:
            print("Valores inválidos")

def mostrarMatrir(matriz):
    print("-"*60)
    for i in matriz:
        print(i)
    print("-"*60)


def main():
    matriz = criarMatriz()
    mostrarMatrir(matriz)

main()
