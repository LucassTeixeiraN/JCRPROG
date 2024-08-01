'''
Escreva uma função recursiva que, dado um número inteiro positivo n, retorne a
representação binária de n; e outra função recursiva que, dado um número binário,
retorne a sua representação em decimal.
'''
def binario(N):
    binlist = []
    if N < 0:
        return "ERRO: Digite um numero inteiro positivo"
    while N != 0:
        x = N % 2
        binlist.append(str(x))
        N = N // 2
    binlist.reverse()
    binario_str = "".join(binlist)
    return binario_str

def binario_para_decimal(binario):
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "ERRO: Insira um número binário válido (composto apenas por 0s e 1s)."

def menu():
    while True:
        print("-" * 32, "MENU", "-" * 32)
        print("1- Converter decimal para binário")
        print("2- Converter binário para decimal")
        print("3- Sair")
        print("-" * 70)

        opcao = int(input("Digite a opção desejada: "))

        if opcao < 1 or opcao > 3:
            print("\t\nValor inválido.")
        return opcao

def main():
    while True:
        print("\nAperte Enter para ir ao Menu.")
        try:
            if input("") == "":
                escolha = menu()
                if escolha == 1:
                    print("-" * 70)
                    N = int(input("Digite o número decimal: "))
                    if N >= 0:
                        print(f"O número {N} em binário é: {binario(N)}")
                    else:
                        print(binario(N))
                        continue
                    print("-" * 70)
                elif escolha == 2:
                    print("-" * 70)
                    X = input("Digite o número binário: ")
                    print(f"O número binário {X} em decimal é: {binario_para_decimal(X)}")
                    print("-" * 70)
                elif escolha == 3:
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
