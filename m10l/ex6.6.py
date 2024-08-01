'''
Escreva uma função recursiva que, dado um número inteiro positivo n, retorne a
representação binária de n; e outra função recursiva que, dado um número binário,
retorne a sua representação em decimal.
'''
def decbin(numero):
    if numero == 0:
        return '0'
    elif numero == 1:
        return '1'
    else:
        return decbin(numero//2) + str(numero%2) 
    
def bindec(numero, expoente, indice = 0):
    algarismo = int(numero[indice])

    if indice == len(numero)-1:
        if algarismo == 0:
            return 0
        return 1

    return algarismo*(2**expoente) + bindec(numero, expoente - 1, indice + 1)


def menu():
    while True:
        print("-" * 32, "MENU", "-" * 32)
        print("1- Converter decimal para binário")
        print("2- Converter binário para decimal")
        print("3- Sair")
        print("-" * 70)

        opcao = input("Digite a opção desejada: ")

        return opcao

def main():
    while True:
        print("\nAperte Enter para ir ao Menu.")
        try:
            if input("") == "":
                escolha = menu()
                if escolha == '1':
                    print("-" * 70)
                    N = int(input("Digite o número decimal: "))

                    if N >= 0:
                        print(f"O número {N} em binário é: {decbin(N)}")
                    else:
                        print("Insira valores positivos")
                        continue
                    print("-" * 70)

                elif escolha == '2':
                    print("-" * 70)
                    X = input("Digite o número binário: ")
                    verifBin = True
                    for i in range(len(X)):
                        if X[i] != '0' and X[i] != '1':
                            verifBin = False

                    if verifBin == True:
                        expoente = len(X)-1
                        print(f"O número binário {X} em decimal é: {bindec(X, expoente)}")
                        print("-" * 70)
                    else:
                        print("Insira apenas números binários")

                elif escolha == '3':
                    print("Saindo do programa.")
                    break

                else:
                    print("Opção inválida.")
            else:
                print("")
                continue
        except ValueError:
            print("\nInsira valores válidos")
main()
