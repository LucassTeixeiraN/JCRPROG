# Dadas duas listas L1 e L2, com n e m valores inteiros, respectivamente, escreva um
# programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
# a lista L3 ordenada de maneira crescente e decrescente.

l1 = []
l2 = []

n = input("Insira a quantidade de elementos que a primeira lista terá: ")
m = input("Insira a quantidade de elementos que a segunda lista terá: ")

if not n.isalpha() and n.find(".") == -1 and int(n) > 0 and not m.isalpha() and m.find(".") and int(m) > 0:
    print("Insira os valores numéricos da primeira lista (qualquer outro valor será considerado 0)")
    for i in range(int(n)):
        numero = input()
        if not numero.isalpha():
            l1.append(float(numero))
        else:
            l1.append(0)

    print("Insira os valores numéricos da segunda lista (qualquer outro valor será considerado 0)")
    for i in range(int(m)):
        numero = input()
        if not numero.isalpha():
            l2.append(float(numero))
        else:
            l2.append(0)

    l3 = l1+l2
    l3.sort()

    print("-"*25)
    print("Lista 1:", l1)
    print("Lista 2:", l2)
    print("Lista 3:", l1+l2)
    print("Lista 3 em ordem crescente:", l3)
    print("Lista 3 em ordem decrescente:", l3[::-1])
else:
    print("Os valores inseridos não são válidos, insira valores numéricos inteiros")

