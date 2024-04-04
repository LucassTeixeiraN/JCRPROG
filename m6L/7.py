# Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto
# que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em
# branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto:
# número de caracteres digitados, número de espaços em branco e número de linhas

matriz = []
n_carac = n_espacos = n_linhas = 0


while True:
    texto = input()
    linha = []

    if texto == "":
        break

    for i in range(len(texto)):
        linha.append(texto[i])
        
    matriz.append(linha)

n_linhas = len(matriz)

for i in range(len(matriz)):
    print(matriz[i])
    for j in range(len(matriz[i])):
        if matriz[i][j] == " ":
            n_espacos += 1
        else:
            n_carac += 1




print("-"*15)
print("Número de caracteres digitados:", n_carac)
print("Número de espaços em branco:", n_espacos)
print("Número de linhas:", n_linhas)
print("-"*15)