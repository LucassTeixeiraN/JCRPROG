'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
triangular inferior.'''

def criarMatriz():
    ordem = input("Insira o número de linhas e colunas da matriz quadrada")
    matriz = []

    if ordem.isnumeric() and int(ordem) > 0:
        ordem = int(ordem)

        for i in range(ordem):
            linha = []
            for j in range(ordem):
                while True:
                    try:
                        valor = input(f"Insira o valor [{i + 1}, {j + 1}]: ")
                        linha.append(int(valor))
                        break
                    except ValueError:
                        print("Valor inválido")
            matriz.append(linha)
        
        return matriz

def matrizTriang():
    matriz = criarMatriz()

    triangular = True
    zerosNecessarios = len(matriz[0]) - 1
    
    for i in range(len(matriz)):
        sequencia = True
        zerosPorLinha = 0
        print(matriz[i])

        for j in matriz[i]:
            #Verifica se a penultima linha começa com zero
            if matriz[len(matriz)-2][0] == 0:
                #Contabiliza os zeros que aparecem em sequência
                if j == 0 and sequencia == True:
                    zerosPorLinha += 1
                else:
                    sequencia = False

            #Verifica se a penultima linha termina com zero
            elif matriz[len(matriz)-2][len(matriz[i])-1] == 0:
                #Contabiliza os zeros que aparecem, caso algum número diferente de zero seja analisado, a variável é redefenida para zero
                if j == 0:
                    zerosPorLinha += 1
                else:
                    zerosPorLinha = 0

            #Caso a segunda linha não comece ou termine com zero
            else:
                triangular = False

        # Se a quantidade de zeros necessários por linha seja diferente da quantidade contada, a matriz não é triangular
        if zerosNecessarios != zerosPorLinha:
            triangular = False
        
        zerosNecessarios -= 1
    
    if triangular == True:
        print("A matriz é triangular inferior")
    else:
        print("A matriz não é triangular inferior")


def main():
    matrizTriang()

main()
