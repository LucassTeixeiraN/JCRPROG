# Faça um programa que calcule o Máximo Divisor Comum entre dois números.

n1 = int(input("Insira um primeiro número para o calculo do MDC (inteiro > 0): "))
n2 = int(input("Insira um segundo número para o calculo do MDC (inteiro > 0): "))

mdc = n1
while n1 % mdc != 0 or n2 % mdc != 0:
    mdc -= 1

print("O MDC de " + str(n1) + " e " + str(n2) + " é " + str(mdc))