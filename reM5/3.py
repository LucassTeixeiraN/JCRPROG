# Faça um programa para calcular a média de um conjunto de 15 valores dados pelo
# usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores
# digitados que ficaram abaixo da média.

valores = []
valores_abaixo_da_media = []
N_VALORES = 15

print("Insira valores numéricos reais (Pressione ENTER entre os valores)")
i = 0
while i < N_VALORES:
    valor = input()
    if not valor.isalpha():
        valores.append(float(valor))
        i += 1
    else:
        print("Número inválido")

media = sum(valores)/N_VALORES

for i in valores:
    if i < media:
        valores_abaixo_da_media.append(i)

print("-"*25)
print("Média:", round(media, 2))
print("Valores que ficaram abaixo da média:")
print(valores_abaixo_da_media)
print("-"*25)