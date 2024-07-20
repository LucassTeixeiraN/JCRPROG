'''14. Faça um programa que apresente na tela um menu com as seguintes opções: 1 –
converter um ângulo em graus para radiano; 2 - calcular o seno de um ângulo, 3 –
calcular o valor de . 4 - resolver uma equação do segundo grau; 0 - sair. Depois de
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já
implementou.'''



def exibir_menu():
    print("Menu:")
    print("1 - Converter um ângulo em graus para radianos")
    print("2 - Calcular o seno de um ângulo")
    print("3 - Mostrar o valor de π")
    print("4 - Resolver uma equação do segundo grau")
    print("0 - Sair")

# Coverte de graus para radiano
def converter_graus_para_radianos(grau):
    rad = grau/180
    return rad

# Calcula o seno de um ângulo
def calcular_seno(grau):
    rad = converter_graus_para_radianos(grau)
    PRECISAO = 10

    seno = 0

    n = 1
    for i in range(PRECISAO):
        fatorial = 1
        for j in range(1, n+1):
            fatorial *= j

        seno += ((rad*3.14)**n)/fatorial
        n += 2
    return seno

# Calcula o valor de pi apartir de uma precisão fornecida
def mostrar_valor_pi(precisao):
    pi_aproximado = 0
    sinal = 1

    for i in range(1, precisao + 1):
        termo = 4 / (2 * i - 1) 
        pi_aproximado += sinal * termo 
        sinal *= -1 

    return pi_aproximado

# Resolve uma equação de segundo grau
def resolver_equacao_segundo_grau(a, b, c):
    
    delta = b**2 - 4*a*c

    if delta > 0:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"A equação tem duas raízes reais:")
        print(f"Raiz 1 (x1) = {raiz1}")
        print(f"Raiz 2 (x2) = {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação tem uma raiz real (raiz dupla):")
        print(f"Raiz (x) = {raiz}")
    else:
        print("A equação não tem raízes reais.")

# Menu com opções
def menu():
    while True:
        print("-"*60)
        if input("Pressione ENTER para mostrar as opções") == "":
            exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        #grau para radiano
        if opcao == '1':
            try:
                print("-"*60)
                x = int(input("Insira um valor em graus para ser convertido para radiano: "))
                print()
                rad = converter_graus_para_radianos(x)
                print(f'45° = {rad}π rad')
            except ValueError:
                print("Valores inválidos")

        #seno de um ângulo
        elif opcao == '2':
            try:
                print("-"*60)
                x = int(input("Insira um valor em graus para ser convertido para radiano: "))
                print()
                seno = calcular_seno(x)
                print(f'sen {x}° = {seno}')
            except ValueError:
                print("Valores inválidos")
        
        #Calculo de pi
        elif opcao == '3':
            while True:
                try:
                    print("-"*60)
                    precisao = int(input("Insira a precisão desejada (numero inteiro): "))
                    print()
                    pi = mostrar_valor_pi(precisao)
                    print(f'π = {pi}')
                    break
                except ValueError:
                    print("Valor inválido")

        #Equação de segundo grau
        elif opcao == '4':
            try:
                print("-"*60)
                a = float(input("Informe o valor de a: "))
                b = float(input("Informe o valor de b: "))
                c = float(input("Informe o valor de c: "))
                print()
                resolver_equacao_segundo_grau(a, b, c)
            except ValueError:
                print("Valores inválidos")

        #Sair do programa
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def main():
    menu()

main()
