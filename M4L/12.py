# Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N
# é fornecido pelo usuário.
# Sabemos que:
# N! = 1 x 2 x 3 x 4 x. . .x (N - 1) x N;
# 0! = 1, por definição.

N = int(input("Insira um número para que seu fatorial seja calculado: "))
resultado = 1 # Variável que a cada loop vai ser multiplicada
calculo = str(N) + "! = 1 x " # Inicio do resultado que será imprimido (N! = 1 x ....), a cada loop o número usado vai ser concatenado a essa variável

if N == 0 or N == 1: # caso o N seja 0 ou 1 será imprimido N! = 1
    calculo = str(N) + "! = 1"

for i in range(2, N+1): 
    resultado = resultado * i # A cada loop essa variável vai ser multiplicada pelo valor de i

    if i != N : # Enquanto o i for diferente do valor final do range, ele vai concatenar o seguinte modelo à variável printada (... i x ......)
        calculo += str(i) + " x "
    else: # No caso do loop estar no último valor do range (i = n) o valor concatenado a váriavel printada será diferente (... i = resultado)
        calculo += str(i) + " = " + str(resultado)

print(calculo)