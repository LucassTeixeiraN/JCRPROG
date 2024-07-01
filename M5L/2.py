# Dadas duas listas L1 e L2, com n e m valores inteiros, respectivamente, escreva um
# programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
# a lista L3 ordenada de maneira crescente e decrescente.

n = input("Insira quantos valores a primeira lista terá (insira números inteiros): ")
m = input("Insira quantos valores a segunda lista terá (insira números inteiros): ")
l1 = []
l2 = []

if n.isnumeric() and m.isnumeric():
    for i in range(int(n)):
        numero = input("Insira os valores para a primeira lista (qualquer valor não númerico será lido como 0): ")
        if numero.startswith("-"):
            x = numero[1:]
            if x.isdigit():
                l1.append(int(numero))
            else:
                l1.append(0)
        else:
            if numero.isdigit():
                l1.append(int(numero))
            else:
                l1.append(0)


    for i in range(int(m)):
        numero = input("Insira os valores para a segunda lista (qualquer valor não númerico será lido como 0): ")
        if numero.startswith("-"):
            x = numero[1:]
            if x.isdigit():
                l2.append(int(numero))
            else:
                l2.append(0)
        else:
            if numero.isdigit():
                l2.append(int(numero))
            else:
                l2.append(0)

    l3 = l1 + l2

    print("-"*12)
    print("Lista 1:",l1)
    print("Lista 2:",l2)
    print("Lista 3:",l3)
    l3.sort()
    print("Lista 3 em ordem crescente:", l3)
    print("Lista 3 em ordem decrescente:", l3[::-1])
    print("-"*12)
else:
    print("Insira números inteiros para os tamanhos das listas")