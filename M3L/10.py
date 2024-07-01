# Faça um programa que lê um caracter do teclado e imprima se o caracter é uma letra.
# Se for, deve imprimir se a letra em questão é maiúscula ou minúscula. Dica: use os
# códigos ASCII das letras para resolver este problema.

letra = input("Insira uma letra: ")

if letra >= "A" and letra <= "Z":
    print("O caracter é uma letra e é maiúscula")
elif letra >= "a" and letra <= "z":
    print("O caracter é uma letra e é minúscula")
else:
    print("O caracter não é uma letra")