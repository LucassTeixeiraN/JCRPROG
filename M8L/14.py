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

def converter_graus_para_radianos(grau):
    
    rad = grau/180
    return rad

def calcular_seno(grau):
    rad = converter_graus_para_radianos(grau)
    PRECISAO = 10

    seno = 0

    # Tentar deixar mais claro esse loop
    n = 1
    for i in range(PRECISAO):
        fatorial = 1
        for j in range(1, n+1):
            fatorial *= j

        seno += ((rad*3.14)**n)/fatorial
        n += 2
    return seno

def mostrar_valor_pi():
    print("3,14")

def resolver_equacao_segundo_grau():
    
    print("Função para resolver equação do segundo grau será implementada aqui")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                x = int(input("Insira um valor em graus para ser convertido para radiano: "))
                rad = converter_graus_para_radianos(x)
                print(f'{rad}π rad')
            except ValueError:
                print("Valores inválidos")

        elif opcao == '2':
            try:
                x = int(input("Insira um valor em graus para ser convertido para radiano: "))
                seno = calcular_seno(x)
                print(seno)
            except ValueError:
                print("Valores inválidos")

        elif opcao == '3':
            mostrar_valor_pi()
        elif opcao == '4':
            resolver_equacao_segundo_grau()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()
