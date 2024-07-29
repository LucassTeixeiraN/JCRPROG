# 1. Escreva uma função que calcule o enésimo número de Fibonacci de forma recursiva,
# a partir de um valor fornecido pelo usuário. Além disso, crie também uma função
# iterativa do Fibonacci e compare a quantidade de somas e a de tempo de execução.

import timeit

def fibonacciRec(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)

def fibonacciCom(n):

    n1 = 0
    n2 = 1
    for i in range(n-1):
        soma = n1 + n2
        n1 = n2
        n2 = soma
    
    return soma

def tempoExec(opcao, numero):

    if opcao == 1:
        inicio = timeit.default_timer()
        fibonacciRec(numero)
        fim = timeit.default_timer()
        tempo_rec = fim - inicio
        return tempo_rec

    inicio = timeit.default_timer()
    fibonacciCom(numero)
    fim = timeit.default_timer()
    tempo_com = fim - inicio
    return tempo_com

    

def main():
    print("-"*60)
    while True:
        try:
            numero = int(input("Insira um valor para saber qual número está nessa posição na sequência de Fibonacci: "))
            print(f'O número que ocupa a {numero}° é: {fibonacciCom(numero)}')
            print(f"A função recursiva demorou {tempoExec(1, numero)} segundos")
            print(f"A função não recursiva demorou {tempoExec(2, numero)} segundos")

            print("-"*60)
            
            break
        except ValueError:
            print("Número inválido. Tente novamente.")

main()