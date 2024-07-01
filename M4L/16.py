# Sendo S = (1/2) + (1/3) + (1/4) + (1/5)... + (1/N) , construa um programa que leia N, 
# calcule e mostreo valor da série S.

n = int(input("Insira um valor para n: "))
soma = 0

for i in range(2, n+1):
    soma += 1/i

print(soma)