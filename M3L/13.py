# Elabore um programa que receba três valores quaisquer e imprima o menor valor dos
# três lidos. O que acontece se o seu programa tiver lido dois ou mais números iguais
# (Ex.: 1, 1, 3)?

a = int(input("Insira um número inteiro qualquer: "))
b = int(input("Insira um número inteiro qualquer: "))
c = int(input("Insira um número inteiro qualquer: "))

if (a == b) or (a == c) or (b == c):
    print("Alguns dos valores são iguais")
elif (a < b) & (a < c):
    print(a)
elif (b < a) & (b < c):
    print(b)
else:
    print(c)

