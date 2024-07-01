# Faça um programa para calcular a média de um conjunto de 15 valores dados pelo
# usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores
# digitados que ficaram abaixo da média.

VALORES = 15
lista = []
abaixo_media = []

print(f"Insira {VALORES} números (aperte Enter entre cada valor)")
i = 0
while i < VALORES:
    user_input = input()
    
    if user_input.isalpha():
        print("Insira um valor válido")
    else:
        lista.append(float(user_input))
        i += 1

media = sum(lista)/VALORES

for i in lista:
    if i < media:
        abaixo_media.append(i)

print("-"*15)
print("A média dos valores inseridos é:", round(media, 2))
print("Os seguintes valores inseridos ficaram abaixo da média:", abaixo_media)
print("-"*15)