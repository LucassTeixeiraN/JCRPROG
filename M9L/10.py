'''Uma matriz quadrada de números inteiros é um quadrado mágico se o valor da soma
dos elementos de cada linha, de cada coluna e da diagonal principal e da diagonal
secundária é o mesmo. Além disso, a matriz deve conter todos os números inteiros
do intervalo [1..n × n]. Escreva um programa que, dada uma matriz quadrada,
verifique se ela é um quadrado mágico.'''

# Cria a matriz apartir de valores fornecidos pelo usuário
def criarMatriz():
    ordem = input("Insira o número de linhas e colunas da matriz quadrada")
    matriz = []

    if ordem.isnumeric() and int(ordem) > 0:
        ordem = int(ordem)

        for i in range(ordem):
            linha = []
            for j in range(ordem):
                valor = input(f"Insira o valor [{i + 1}, {j + 1}]: ")
                linha.append(int(valor))
            matriz.append(linha)
        
        return matriz
    

# Analisa se todas as condições são verdadeiras e a partir disso imprime uma resposta
def main():
    matriz = criarMatriz()
    soma = sum(matriz[0])

    intervalo = valoresNoIntervalo(matriz)
    linhas = somaLinhas(matriz, soma)
    colunas = somaColunas(matriz, soma)
    diag_princ = somaDP(matriz, soma)
    diag_sec = somaDS(matriz, soma)
    print("-"*30)
    print("A matriz: ")
    mostrarMatriz(matriz)
    if intervalo == True and linhas == True and colunas == True and diag_princ == True and diag_sec == True:
        print("É um quadrado mágico")
    else:
        print("Não é um quadrado mágico")


# Verifica se todos os valores da matriz estão no intervalo [1..n*n]
def valoresNoIntervalo(matriz):
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

# Faz a soma de cada linha e verifica se são iguais
def somaLinhas(matriz, soma):

        checagem = True

        for i in matriz:
            if sum(i) != soma:
                checagem = False
        
        return checagem

# Faz a soma de cada coluna e verifica se são iguais
def somaColunas(matriz, soma):

    checagem = True

    transposta = []
    for j in range(len(matriz)):
        linha_transposta = []
        for i in range(len(matriz)):
            elemento_transposto = matriz[i][j]
            linha_transposta.append(elemento_transposto)
        transposta.append(linha_transposta)
    
    for i in transposta:
        if sum(i) != soma:
            checagem = False
    
    return checagem

# Faz a soma diagonal principal e verifica se é igual
def somaDP(matriz, soma):
    checagem = True
    soma_elementos = 0

    i = 0
    n = len(matriz)
    while i < n:
        soma_elementos += matriz[i][i]
        i += 1
    
    if soma_elementos != soma:
        checagem = False
    return checagem

# Faz a soma diagonal secundária e verifica se é igual
def somaDS(matriz, soma):
    checagem = True
    soma_elementos = 0

    i = 0
    j = n = len(matriz)
    
    while i < n:
        soma_elementos += matriz[i][j - 1]
        i += 1
        j -= 1
    
    if soma_elementos != soma:
        checagem = False
    return checagem

# Imprime a matriz fornecida pelo usuário
def mostrarMatriz(matriz):
    for i in matriz:
        print(i)
