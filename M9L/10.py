'''Uma matriz quadrada de números inteiros é um quadrado mágico se o valor da soma
dos elementos de cada linha, de cada coluna e da diagonal principal e da diagonal
secundária é o mesmo. Além disso, a matriz deve conter todos os números inteiros
do intervalo [1..n × n]. Escreva um programa que, dada uma matriz quadrada,
verifique se ela é um quadrado mágico.'''

def criarMatriz(): # Cria a matriz apartir de valores fornecidos pelo usuário
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
    
# Analisa se todas as condições são verdadeiras e a partir disso imprime uma resposta
def valoresNoIntervalo(matriz): # Verifica se todos os valores da matriz estão no intervalo [1..n*n]
    numeros = []
    ordem = len(matriz)

    for i in matriz:
        for j in i:
            numeros.append(j)
    numeros.sort()

    if numeros == list(range(1, (ordem**2)+1)):
        return True
    else:
        return False


def somaLinhas(matriz, soma): # Faz a soma de cada linha e verifica se são iguais
        for i in matriz:
            if sum(i) != soma:
                return False
        return True


def somaColunas(matriz, soma): # Faz a soma de cada coluna e verifica se são iguais
    n = len(matriz)
    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma:
            return False
    return True

def somaDP(matriz, soma): # Faz a soma diagonal principal e verifica se é igual
    soma_elementos = 0
    n = len(matriz)
    for i in range(n):
        soma_elementos += matriz[i][i]
    if soma_elementos != soma:
        return False
    return True


def somaDS(matriz, soma): # Faz a soma diagonal secundária e verifica se é igual
    soma_elementos = 0
    j = n = len(matriz)
    for i in range(n):
        soma_elementos += matriz[i][j - 1]
        j -= 1
    if soma_elementos != soma:
        return False
    return True

def mostrarMatriz(matriz): # Imprime a matriz fornecida pelo usuário
    for i in matriz:
        print(i)

def quadradoMagico():
    matriz = criarMatriz()
    soma = sum(matriz[0])
    if not valoresNoIntervalo(matriz):
        return False
    if not somaLinhas(matriz, soma):
        return False
    if not somaColunas(matriz, soma):
        return False
    if not somaDP(matriz, soma):
        return False
    if not somaDS(matriz, soma):
        return False
    print("-"*30)
    print("A matriz: ")
    mostrarMatriz(matriz)
    return True

def main():
    verifQuadradoMagico = quadradoMagico()

    if verifQuadradoMagico:
        print("A matriz é um quadrado mágico")
    else:
        print("A matriz não é um quadrado mágico")

main()
