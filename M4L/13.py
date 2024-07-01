# A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os
# demais são dados pela soma dos dois anteriores. Faça um programa que imprima os
# “n” primeiros termos da série, sendo “n” dado pelo usuário. 

N = int(input("Insira o número de termos:"))
n1 = n2 = 1
contador = 0

print("Sequência de Fibbonacci:")
while contador < N: # while para deixar o contador ativo até o número de termos inserido pelo usuário
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n 
    contador += 1

print("Quantidade de termos:",N)