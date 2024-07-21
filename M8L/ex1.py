'''Escreva uma função que, dados dois números inteiros positivos, calcule e retorne o
Máximo Divisor Comum (MDC) entre os dois.

Escreva também uma função que, dada uma lista de três ou mais números inteiros positivos, 
calcule e retorne o Máximo
Divisor Comum (MDC) entre eles. A seguir, escreva um programa para testar essas
funções.'''

def mdc(a, b):
    # Teorema de Euclides para calcular o MDC de dois números
    while b != 0:
        # Atualiza 'a' e 'b' simultaneamente: 'a' recebe o valor de 'b' e 'b' recebe o resto da divisão de 'a' por 'b'
        a, b = b, a % b
    return a  # Retorna o MDC

def mdc_lista(numeros):
    # Calcula o MDC de uma lista de números
    resultado = numeros[0]  # Inicializa o resultado com o primeiro número da lista
    for num in numeros[1:]:  # Itera sobre os números restantes na lista
        resultado = mdc(resultado, num)  # Calcula o MDC do resultado atual com o próximo número
    return resultado  # Retorna o MDC final

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
                if a.isdigit() and b.isdigit():  # Verifica se as entradas são números válidos
                    a = int(a)
                    b = int(b)
                    print(f"MDC({a}, {b}) = {mdc(a, b)}")  # Calcula e imprime o MDC
                    print()
                else:
                    print("Insira números válidos")

            # MDC de uma lista de números
            elif opcao == "2":
                print("Digite os números que irão compor sua lista (Pressione ESPAÇO entre cada um): ")
                numeros = input()
                while True:
                    try:
                        lista = [int(num) for num in numeros.split()]  # Converte a entrada em uma lista de inteiros
                        mdcs = mdc_lista(lista)  # Calcula o MDC da lista
                        print(f'MDC de {lista}: {mdcs}')  # Imprime o MDC
                        print()
                        break
                    except ValueError:  # Trata entradas inválidas
                        print("Valores inválidos")
                        break

            # Sair do programa
            elif opcao == "0":
                print("Saindo do programa")
                print("-"*60)
                break

def main():
    menu()  # Chama a função de menu

main()  # Executa o programa
