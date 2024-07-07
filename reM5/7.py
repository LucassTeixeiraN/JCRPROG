# Fazer um programa que calcule e imprima a soma de duas matrizes (a ordem das
# duas matrizes deve ser lida da entrada padrão).
print("-"*75)

m1 = []
m2 = []
soma = []
m = input("Insira o número de linhas da matriz: ")
n = input("Insira o número de colunas da matriz: ")

if m.isdigit() and n.isdigit() and int(m) > 0 and int(n) > 0:
    m = int(m)
    n = int(n)
    
    print("Insira os números da primeira matriz (pressione Enter entre cada número). Obs: Valores não numéricos serão considerados como 0: ")
    for i in range(m):
        linha = []

        for j in range(n):
            elemento = input()

            if not elemento.isalpha() and elemento != "":
                elemento = float(elemento)
                linha.append(elemento)
            else:
                linha.append(0)

        m1.append(linha)
    
    print("Insira os números da segunda matriz (pressione Enter entre cada número). Obs: Valores não numéricos serão considerados como 0: ")
    for i in range(m):
        linha = []

        for j in range(n):
            elemento = input()

            if not elemento.isalpha() and elemento != "":
                elemento = float(elemento)
                linha.append(elemento)
            else:
                linha.append(0)

        m2.append(linha)
    
    
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(m1[i][j] + m2[i][j])
        soma.append(linha)

    print("-"*75)
    for i in range(m):
        if i == m//2:
            print(f"{m1[i]} + {m2[i]} = {soma[i]}")
        else:
            print(f"{m1[i]}   {m2[i]}   {soma[i]}")
    print("-"*75)

else:
    print("-"*75)
    print("Tente inserir valores numéricos inteiros positivos na ordem das matrizes")
    print("-"*75)