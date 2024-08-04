# 2. Usando algoritmos recursivos, escreva funções que:
# a. Some dois números inteiros não negativos, apenas usando incrementos e
# decrementos unitários.
# b. Multiplique dois números inteiros positivos, x e y, usando apenas somas e
# subtrações.
# c. Some todos os inteiros positivos pares menores ou iguais a um valor inteiro n.

def somaUnitaria(a, b):
    if b == 0:
        return a
    return somaUnitaria(a+1, b-1)        

def multiplicacao(a, b):
    if b == 0: 
        return 0
    return a + multiplicacao(a, b-1)


def somaPares(n):
    if n%2 == 1:
        n = n-1
    elif n == 0:
        return 0
    return n + somaPares(n-2)

def menu():
    print("-"*60)
    print("Selecione uma das seguintes opções:")
    print("1 - Some dois números inteiros não negativos, apenas usando incrementos e decrementos unitários.")
    print("2 - Multiplique dois números inteiros positivos, x e y, usando apenas somas e subtrações.")
    print("3 - Some todos os inteiros positivos pares menores ou iguais a um valor inteiro n.")
    print("0 - Sair do programa.")
    opcao = input()
    print("-"*60)
    return opcao

def main():
    while True:
    
        opcao = menu()
        try:
            if opcao == "1":
                n1 = int(input("Insira o primeiro número da soma: "))
                n2 = int(input("Insira o segundo número da soma: "))
                if n1 >= 0 and n2 >= 0:
                    print(f"{n1} + {n2} = {somaUnitaria(n1, n2)}")
                else:
                    print("Insira valores inteiros não negativos")
            elif opcao == "2":
                n1 = int(input("Insira o primeiro número do produto: "))
                n2 = int(input("Insira o segundo número do produto: "))
                if n1 > 0 and n2 > 0:
                    print(f"{n1} * {n2} = {multiplicacao(n1, n2)}")
                else:
                    print("Insira valores inteiros positivos")
            elif opcao == "3":
                n = int(input("Insira n: "))
                if n > 0:
                    print(f"A soma dos números pares de 0 a {n} é {somaPares(n)}")
                else:
                    print("Insira um valor inteiro positivo")

            elif opcao == "0":
                print("Finalizando programa.")
                print("-"*60)
                break
            else:
                print("Opção inválida")

        except ValueError:
            print("Valor inválido")
main()
