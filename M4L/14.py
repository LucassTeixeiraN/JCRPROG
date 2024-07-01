# Construa um programa que calcule e mostre a soma dos 30 primeiros termos da
# série: (450/10)+(445/11)+(440/12)+(435/13)+...

soma = 0
dividendo = 450
divisor = 10

i = 1
while i <= 30:
    soma += dividendo/divisor
    dividendo -= 5
    divisor += 1
    i += 1

print(soma)