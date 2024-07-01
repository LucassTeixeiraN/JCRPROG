# Escreva um programa que, dados três números inteiros, imprima os números em
# ordem crescente.

a = int(input("Insira um número inteiro qualquer: "))
b = int(input("Insira um número inteiro qualquer: "))
c = int(input("Insira um número inteiro qualquer: "))

if (a > b) and (a > c): # a é o maior número
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
elif (b > a) and (b > c): # b é o maior número
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
else: # c é o maior
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c) 