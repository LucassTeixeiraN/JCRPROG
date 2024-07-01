# Faça um programa que leia as dimensões de uma matriz qualquer (no máximo 30x30),
# leia seus elementos e imprima a sua transposta

m = input("Insira o número de linhas da matriz (máximo de 30): ")
n = input("Insira o número de colunas da matriz (máximo de 30): ")


if m.isdigit() and n.isdigit():
    m = int(m)
    n = int(n)
    # Verificar se as dimensões da matriz estão dentro do limite máximo
    if m > 30 or n > 30 or m < 0 or n < 0:
        print("As dimensões da matriz excedem o limite máximo permitido.")
    else:
        # Cria a matriz
        matriz = []
        print("Insira os elementos da matriz:")
        for i in range(m):
            linha = []
            for j in range(n):
                elemento = float(input(f"Insira o elemento da posição ({i + 1}, {j + 1}): "))
                linha.append(elemento)
            matriz.append(linha)

        # Calcular a transposta da matriz
        transposta = []
        for j in range(n):
           linha_transposta = []
           for i in range(m):
               elemento_transposto = matriz[i][j]
               linha_transposta.append(elemento_transposto)
           transposta.append(linha_transposta)
else:
    print("Insira apenas numeros validos")

# Imprimir a matriz original
print("\nMatriz original:")
for linha in matriz:
    print(linha)

# Imprimir a transposta da matriz
print("\nTransposta da matriz:")
for linha in transposta:
   print(linha)