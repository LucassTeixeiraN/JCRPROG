# Seja o polinômio: P(X) = anX^n + an-1X^n-1 + an-2X^n-2 + ... + a1X + a0
# Escreva um programa que leia um número real x, a ordem do polinômio n (no máximo
# 20), os coeficientes ai e calcule o resultado. Imprima o polinômio lido e o valor
# calculado. 
print("-"*90)
print("No formato do seguinte polinômio: P(X) = anX^n + an-1X^n-1 + an-2X^n-2 + ... + a1X + a0")
x = input("Insira o valor para X (Qualquer valor real): ")
n = input("Insira a ordem do polinômio (Qualquer valor inteiro positivo e menor ou igual a 20): ")
coeficientes = []

polinomio = f"P({x}) = "
soma = 0

if not x.isalpha() and n.isnumeric() and 0 < int(n) <= 20:

    if x.find(".") == -1:
        x = int(x)
    else:
        x = float(x)

    n = int(n)

    print("Insira os coeficientes do polinômio (Aperte ENTER entre cada número). Obs.: caractéres inválidos serão lidos como 0")
    while n >= 0:

        coef = input()
        if not coef.isalpha():
            if coef.find(".") == -1:
                coeficientes.append(int(coef))
            else:
                coeficientes.append(float(coef))
        else:
            coeficientes.append(0)

        soma += coeficientes[-1] * x**n

        if n != 0:
            polinomio += f'{coeficientes[-1]} x {x}^{n} + '
        else:
            polinomio += f'{coeficientes[-1]} = {soma}'
        n -= 1
    
    print("-"*90)
    print(polinomio)
    print("-"*90)
    
else:
    print("Insira valores válidos para X e para a ordem do polinômio")