# Escreva um programa que leia os três lados de um triângulo e imprima se o triângulo
# é equilátero, isósceles ou escaleno, ou ainda, se estes lados não podem constituir um
# triângulo.
# Lembre-se que:
# • O comprimento de cada lado de um triângulo é sempre menor do que a soma
# dos comprimentos dos outros dois lados.
# • Triângulo equilátero: três lados iguais.
# • Triângulo isósceles: dois lados iguais.
# • Triângulo escaleno: três lados diferentes

a = float(input("Insira o primeiro lado do triângulo: "))
b = float(input("Insira o segundo lado do triângulo: "))
c = float(input("Insira o terceiro lado do triângulo: "))

if (a <= b+c) and (b <= c+b) and (c <= b+a):
    if (a == c) and (a == b) and (b == c):
        print("O triângulo é equilátero")
    elif(a != b) and (a != c) and (b != c):
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isóceles")
else:
    print("Os lados inseridos não formam um triângulo")