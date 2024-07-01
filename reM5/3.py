# Faça um programa para calcular a média de um conjunto de 15 valores dados pelo
# usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores
# digitados que ficaram abaixo da média.

valores = []
valores_abaixo_da_media = []
N_VALORES = 15

print("Insira valores numéricos reais (qualquer outro será considerado 0)")
for i in range(N_VALORES):
    valor = input()
    if not valor.isalpha():
        valores.append(float(valor))
    else:
        valores.append(0)

media = sum(valores)/N_VALORES

for i in valores:
    if i < media:
        valores_abaixo_da_media.append(i)

print("-"*25)
print("Média:", round(media, 25))
print("Valores que ficaram a baixo da média:")
print(valores_abaixo_da_media)
print("-"*25)