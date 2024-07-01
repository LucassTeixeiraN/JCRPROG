# Crie um programa que leia uma frase e, a seguir, imprima:
# a. Quantos caracteres foram digitados.
# b. Quantos espaços brancos existem na frase.
# c. Quantos desses caracteres são minúsculos e quantos são maiúsculos.
# d. Quantos desses caracteres são dígitos.
# e. Quantos desses caracteres são de pontuação.

frase = input("Insira uma frase para ser analisada: ")
PONTUACAO = ('.', ',', ':', ';', '!', '?')
n_maiusc = n_minusc = n_digit = n_pont =0

for i in range(len(frase)):
    if frase[i].isdigit():
        n_digit += 1
    elif frase[i].isalpha() and frase[i].lower() == frase[i]:
        n_minusc += 1
    elif frase[i].isalpha() and frase[i].upper() == frase[i]:
        n_maiusc += 1
    elif frase[i] in PONTUACAO:
        n_pont += 1


print("-"*65)
print(f"Frase: {frase}")
print(f"Número de caractéres digitados: {len(frase)}")
print(f"Número de espaços: {frase.count(" ")}")
print(f"Número de caractéres minúsculos: {n_minusc}")
print(f"Número de caractéres maiúsculos: {n_maiusc}")
print(f"Número de dígitos: {n_digit}")
print(f"Número de pontuações: {n_pont}")
print("-"*65)