# Seja o polinômio: P(X) = anX^n + an-1X^n-1 + an-2X^n-2 + .... + a1X + a0
# Escreva um programa que leia um número real x, a ordem do polinômio n (no máximo
# 20), os coeficientes ai e calcule o resultado. Imprima o polinômio lido e o valor
# calculado.

n = input("Insira um número inteiro para n (máx. 20): ")
x = input("Insira um valor real para x: ")
a_list = []
resposta = 0
p = f"P({x}) = "

# Verifica se n e x são números
if n.isalpha() and x.isalpha():
    print("O valor inserido não é válido")
else:

    n = int(n)
    x = float(x)

    #Verifica se n está entre 0 e 20
    if n > 20 or n < 0:
        print("Insira um número de 0 a 20 para o n")
    else:
        i = 0
        print("Insira uma lista de números para serem os coeficientes de X (pressione ENTER entre os número):")
        # Loop para armazenar os valores dos coeficientes em uma lista
        while i <= n:
            a_digit = input()

            #Verifica se a_digit é um número
            if a_digit.isalpha():
                print("O valor inserido não é válido")
                p = ""
                break
            else:
                a_digit = float(a_digit)
                a_list.insert(0, a_digit)
                
            i += 1

        # Loop para calcular o resultado do polinômio e concatenar as strings para montar o polimômio em si
        for a in a_list:
            resposta += a*x**(n)

            if n > 0:
                p += str(a) + " x " + str(x) + "^" + str(n) + " + "
            else:
                p += str(a) + " x " + str(x) + "^" + str(n) + " = " + str(resposta)
            n -= 1

        print(p)