# Crie um programa que leia uma frase e, a seguir, imprima:
# a. Quantos caracteres foram digitados.
# b. Quantos espaços brancos existem na frase.
# c. Quantos desses caracteres são minúsculos e quantos são maiúsculos.
# d. Quantos desses caracteres são dígitos.
# e. Quantos desses caracteres são de pontuação.
texto = input("Insira uma frase para ser analizada: ")
PONTUACOES = (".", ",", ":", ";", "!", "?")
n_espacos = n_min = n_mai = n_digitos = n_pont = 0
n_carac = len(texto)

for i in range(n_carac):
    if texto[i] == " " or texto[i] == "\n" or texto[i] == "\t":
        n_espacos += 1
    elif texto[i] in PONTUACOES:
        n_pont += 1
    elif texto[i].isdigit():
        n_digitos += 1
    elif texto[i] == texto[i].lower():
        n_min += 1
    elif texto[i] == texto[i].capitalize():
        n_mai += 1

print("-"*15)
print("Número de caracteres:", n_carac)
print("Número de espaços em brancos:", n_espacos)
print("Número de caracteres minúsculos:", n_min)
print("Número de caracteres maiúsculos:", n_mai)
print("Número de dígitos:", n_digitos)
print("Número de pontuações:", n_pont)
print("-"*15)