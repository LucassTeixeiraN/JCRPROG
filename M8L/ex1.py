'''Escreva uma função que, dados dois números inteiros positivos, calcule e retorne o
Máximo Divisor Comum (MDC) entre os dois.

Escreva também uma função que, dada uma lista de três ou mais números inteiros positivos, 
calcule e retorne o Máximo
Divisor Comum (MDC) entre eles. A seguir, escreva um programa para testar essas
funções.'''

def mdc(a, b):
    # Teorema de Euclides
    while b != 0:
        # As variáveis são salvas simultaneamente
        a, b = b, a % b
    return a

def mdc_lista(numeros):
    
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mdc(resultado, num)
    return resultado

def menu():
    while True:
        if input("Pressione ENTER para mostrar o Menu") == "":
            print("-"*60)
            print("Selecione uma opção:")
            print("1 - MDC de dois números:")
            print("2 - MDC de uma lista de números:")
            print("0 - Sair do programa\n")
            opcao = input()

            # MDC de 2 números
            if opcao == "1":
                print("-"*60)
                a = input("Digite o primeiro número: ")
                b = input("Digite o segundo número: ")
                if a.isdigit() and b.isdigit():
                    a = int(a)
                    b = int(b)
            
                    print(f"MDC({a}, {b}) = {mdc(a, b)}")
                    print()
                else:
                    print("Insira um números válidos")


            #MDC de uma lista de números
            elif opcao == "2":
                print("Digite os números que irão compor sua lista (Pressione ESPAÇO entre cada um): ")
                numeros = input()

                while True:
                    try:
                        lista = [int(num) for num in numeros.split()]
                        mdcs = mdc_lista(lista)
                        print(f'MDC de {lista}: {mdcs}')
                        print()
                        break
                    except ValueError:
                        print("Valores inválidos")
                        break

            # Sair do programa
            elif opcao == "0":
                print("Saindo do programa")
                print("-"*60)
                break

def main():

    menu()

main()
