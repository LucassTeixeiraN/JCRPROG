'''14. Faça um programa que apresente na tela um menu com as seguintes opções: 1 –
converter um ângulo em graus para radiano; 2 - calcular o seno de um ângulo, 3 –
calcular o valor de . 4 - resolver uma equação do segundo grau; 0 - sair. Depois de
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já
implementou.'''

# Função para exibir o menu de opções
def exibir_menu():
    print("Menu:")
    print("1 - Converter um ângulo em graus para radianos")
    print("2 - Calcular o seno de um ângulo")
    print("3 - Mostrar o valor de π")
    print("4 - Resolver uma equação do segundo grau")
    print("0 - Sair")

# Função para converter graus para radianos (a ser implementada)
def converter_graus_para_radianos():
    print("Graus para radiano incompleto")

# Função para calcular o seno de um ângulo (a ser implementada)
def calcular_seno():
    print("Calcular seno incompleto")

# Função para mostrar o valor de π
def mostrar_valor_pi():
    print("3,14")

# Função para resolver uma equação do segundo grau (a ser implementada)
def resolver_equacao_segundo_grau():
    print("Função para resolver equação do segundo grau será implementada aqui")

# Função principal para exibir o menu e chamar as funções correspondentes
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            converter_graus_para_radianos()
        elif opcao == '2':
            calcular_seno()
        elif opcao == '3':
            mostrar_valor_pi()
        elif opcao == '4':
            resolver_equacao_segundo_grau()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chama a função principal se o script for executado diretamente
main()

