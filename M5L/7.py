# Fazer um programa que calcule e imprima a soma de duas matrizes (a ordem das
# duas matrizes deve ser lida da entrada padrão).

m = input("Insira quantas linhas a matriz terá: ")
n = input("Insira quantas colunas a matriz terá: ")
m1 = []
m2 = []
m3 = []

# Verifica se m e n são números
if m.isdigit() and n.isdigit():
    m = int(m)
    n = int(n)

    i = j = k = 0
    # Loop que salva os valores da primeira matriz
    print("Insira os valores da primeira matriz (da esquerda para a direita e de cima para baixo): ")
    while i < m*n:
        x = input()
        if x.isdigit():
            m1.append(int(x))
        else:
            print("Os valores inseridos não são válidos")
            break
        i += 1

    # Loop que salva os valores da segunda matriz
    print("Insira os valores da segunda matriz (da esquerda para a direita e de cima para baixo): ")
    while j < m*n:
        x = input()
        if x.isdigit():
            m2.append(int(x))
        else:
            print("Os valores inseridos não são válidos")
            break
        j += 1

    # Loop que soma as matrizes e salva os valores em uma terceira matriz
    while k < m*n:
        m3.append(m1[k] + m2[k])
        k += 1

    print('-'*15)
    
    for i in range(m):
        a = []
        
        for j in range(n):
            a.append(m1[j])

        # Remove os elementos usados
        for k in range(n):
            m1.pop(0)
        print(a)
    
    print("\n" + " "*(m+1) + "+" + "\n")

    for i in range(m):
        a = []
        for j in range(n):
            a.append(m2[j])

        for k in range(n):
            m2.pop(0)
        print(a)

    print("\n" + " "*(m+1) + "=" + "\n")

    for i in range(m):
        a = []
        for j in range(n):
            a.append(m3[j])

        for k in range(n):
            m3.pop(0)
        print(a)

    print('-'*15)

else:
    print("Os valores inseridos não são válidos")    