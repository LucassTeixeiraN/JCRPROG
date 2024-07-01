# Faça um programa que leia o ano de nascimento de uma pessoa e imprima se ela é
# maior ou menor de idade. Declare o ano atual e o limite de maioridade como
# constantes simbólicas.

ano_atual = 2024
limite_de_maioridade = 18
ano_de_nascimento = int(input("Insira seu ano de nascimento: "))

if ano_atual - ano_de_nascimento >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
