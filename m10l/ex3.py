''' 
Usando algoritmos recursivos, escreva funções que:
a. Calcule o produtório de um número m, n vezes.
b. Calcule a potência n de um número k.
c. Some os dígitos de um número inteiro não negativo.
d. Calcule a média dos dígitos de um número inteiro não negativo
'''

def produtorio(m, n): 
    if n == 0: 
        return 1
    return m * produtorio(m, n - 1)

def potencia(k, n):
    if n == 0:
        return 1
    return k * potencia(k, n - 1)

def soma(x):
    if x == 0:
        return 0
    else:
        return (x % 10) + soma(x // 10)

def cont(y):
    if y == 0:
        return (0,0)
    soma, quantidade = cont(y // 10)
    return (soma + (y % 10), quantidade + 1)

def media(y):
    soma, quantidade = cont(y)
    if quantidade == 0:
        return 0
    return soma / quantidade


def menu():
    
    opcao = -1
    while opcao < 1 or opcao > 4:
        print("-"*32,"MENU","-"*32)
        print("1- Calcular o produtório de um número ", "2- Calcular a potência de um número ", "3- Some os dígitos de um número inteiro ", "4- Calcule a média dos dígitos de um número inteiro ", "5- Sair do progama", sep="\n")
        print("-"*70)

        opcao = input("Digite a opção desejada: ")

        return opcao

def main():
        while True:
            print("Aperte Enter para ir ao Menu.")
            try:
                if input("") == "":
                    escolha = menu()
                    if escolha == '1':    
                            m = float(input("Insira um número: "))
                            n = int(input("Insira a quantidade de vezes que o número será multiplicado: "))
                            resultado = produtorio(m, n)
                            print(f"O produtório de {m}, {n} vezes é = {resultado:.2f}")
                    elif escolha == '2':
                        k = float(input("Insira um número: "))
                        n = int(input("Insira o expoente: "))
                        resultado = potencia(k, n)
                        print(f"A potência de {k} elevado a {n} é: {resultado:.2f}")
                    elif escolha == '3':
                        x = int(input("Insira um número inteiro não negativo: "))
                        if x >= 0:
                            resultado = soma(x)
                            print(f"A soma dos dígitos de {x} é: {resultado}")
                        else:
                            print("\nInsira apenas valores positivos\n")
                    elif escolha == '4':
                        y = int(input("Insira um número inteiro não negativo: "))
                        if y >= 0:
                            resultado = media(y)
                            print(f"A média dos dígitos de {y} é: {resultado}")
                        else:
                            print("\nInsira apenas valores positivos\n")
                    elif escolha == '5':
                        print("Saindo do programa.")
                        break
                    else:
                        print("\t\nValor inválido")
                else:
                    continue
            except ValueError:
                print("\nInsira valores válidos\n")
main() 
