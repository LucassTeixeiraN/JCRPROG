# Dadas duas listas L1 e L2, com n e m valores inteiros, respectivamente, escreva um
# programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
# a lista L3 ordenada de maneira crescente e decrescente.

l1 = []
l2 = []

n = input("Insira a quantidade de elementos que a primeira lista terá: ")
m = input("Insira a quantidade de elementos que a segunda lista terá: ")

if n.isnumeric() and int(n) > 0 and m.isnumeric() and int(m) > 0:
    n = int(n)
    m = int(m)

    print("Insira os valores numéricos da primeira lista (Pressione ENTER entre cada número)")
    i = 0
    while i < n:
        numero = input()
        if not numero.isalpha():
            l1.append(float(numero))
            i += 1
        else:
            print("Número inválido")


    print("Insira os valores numéricos da segunda lista (Pressione ENTER entre cada número)")
    j = 0
    while j < m:
        numero = input()
        if not numero.isalpha():
            l2.append(float(numero))
            j += 1
        else:
            print("Número inválido")


    l3 = l1+l2

    print("-"*60)
    print("Lista 1:", l1)
    print("Lista 2:", l2)
    print("Lista 3:", l3)
    l3.sort()
    print("Lista 3 em ordem crescente:", l3)
    print("Lista 3 em ordem decrescente:", l3[::-1])
    print("-"*60)
else:
    print("Os valores inseridos não são válidos, insira valores numéricos inteiros")

