# Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto
# que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em
# branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto:
# número de caracteres digitados, número de espaços em branco e número de linhas.

texto = []
n_carac = n_espacos = 0

print("Insira o texto (aperte ENTER em uma linha vazia para finalizá-lo):")
while True:
    linha = input()

    if linha == "":
        break

    n_carac += len(linha)
    n_espacos += linha.count(" ")
    texto.append(linha)

print("-"*65)
print("Texto:")
for i in texto:
    print(i)
print(f"\nNúmero de caractéres: {n_carac}")
print(f"Número de espaços em branco: {n_espacos}")
print(f"Número de linhas: {len(texto)}")
print("-"*65)
