# Uma equação do segundo grau é descrita genericamente por ax2 + bx + c = 0.
# Escrever um programa que leia os valores de a, b e c e resolva a equação do segundo
# grau correspondente, imprimindo as raízes reais quando existirem ou avisando que
# não existem raízes. 


print("Seguindo o padrão ax2 + bx + c = 0")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:
    raiz = -b/(2*a)
    print("A raiz da equação é igual à", raiz)
else:
    raiz1 = (-b+delta**(1/2))/(2*a)
    raiz2 = (-b-delta**(1/2))/(2*a)
    print("As raízes da equação são", raiz1, "e", raiz2)


# delta > 0 => a = 1, b = 3 e c = – 4.
# delta = 0 => a = 1, b = – 6 e c = 9.
# delta < 0 => a = 1, b = 5 e c = 7.