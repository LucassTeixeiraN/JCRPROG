'''Uma equação do segundo grau é escrita
ax**2 + bx + c = 0
e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva
uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.'''


def equacao(a, b, c):
    
    delta = b**2 - 4*a*c

    if delta > 0:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        return 2, raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return 1, raiz
    else:
        return 0  # Nenhuma raiz real

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))
resultado = equacao(a, b, c)

if resultado[0] == 2:
    raiz1, raiz2 = resultado[1], resultado[2]
    print(f"A equação tem duas raízes reais:")
    print(f"Raiz 1 (x1) = {raiz1}")
    print(f"Raiz 2 (x2) = {raiz2}")
elif resultado[0] == 1:
    raiz = resultado[1]
    print(f"A equação tem uma raiz real (raiz dupla):")
    print(f"Raiz (x) = {raiz}")
else:
    print("A equação não tem raízes reais.")
