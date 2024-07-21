'''Escreva as seguintes funções:
a. CparaF – faz a conversão de uma temperatura em graus C para graus F.
b. CparaK – faz a conversão de uma temperatura em C para Kelvin (C=K-273)
c. KparaC – faz a conversão de K para C.
d. KparaF – faz a conversão de K para F (dica: utilize as funções anteriores)
e. FparaK – faz a conversão de F para K.
A seguir, faça um programa que apresente continuamente um menu na tela com
todas as opções de conversão que você implementou. Uma vez feita a opção, o
programa lê do teclado o valor a ser convertido e imprime o resultado '''
# Função para converter Celsius para Fahrenheit
def CparaF(Celsius):
    return (Celsius * 9/5) + 32  # Fórmula de conversão de Celsius para Fahrenheit

# Função para converter Celsius para Kelvin
def CparaK(Celsius):
    return Celsius + 273  # Fórmula de conversão de Celsius para Kelvin

# Função para converter Kelvin para Celsius
def KparaC(Kelvin):
    return Kelvin - 273  # Fórmula de conversão de Kelvin para Celsius

# Função para converter Kelvin para Fahrenheit
def KparaF(Kelvin):
    celsius = KparaC(Kelvin)  # Converte Kelvin para Celsius
    return CparaF(celsius)  # Converte Celsius para Fahrenheit

# Função para converter Fahrenheit para Kelvin
def FparaK(Fahrenheit):
    celsius = (Fahrenheit - 32) * 5/9  # Converte Fahrenheit para Celsius
    return celsius + 273  # Converte Celsius para Kelvin

# Função para obter a entrada do usuário e garantir que seja um número válido
def obter_entrada_usuario():
    while True:
        entrada = input("Digite um valor numérico: ")
        try:
            valor = float(entrada)  # Tenta converter a entrada para um número float
            return valor  # Retorna o valor se for válido
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")  # Mensagem de erro para entradas não numéricas

# Função principal para exibir o menu e realizar as conversões
def main():
    while True:
        print("-"*60)
        print("Escolha qual conversão você deseja fazer:")
        print("1- Celsius para Fahrenheit")
        print("2- Celsius para Kelvin")
        print("3- Kelvin para Celsius")
        print("4- Kelvin para Fahrenheit")
        print("5- Fahrenheit para Kelvin")
        print("S- Sair do programa")
        opcao = input()

        if opcao == '1':
            print("-"*60)
            celsius = obter_entrada_usuario()
            print(f"{celsius}°C = {CparaF(celsius)}°F")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)

        elif opcao == '2':
            print("-"*60)
            celsius = obter_entrada_usuario()
            print(f"{celsius}°C = {CparaK(celsius)}K")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao == '3':
            print("-"*60)
            kelvin = obter_entrada_usuario()
            print(f"{kelvin}K = {KparaC(kelvin)}°C")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)

        elif opcao == '4':
            print("-"*60)
            kelvin = obter_entrada_usuario()
            print(f"{kelvin}K = {KparaF(kelvin)}°F")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao == '5':
            print("-"*60)
            fahrenheit = obter_entrada_usuario()
            print(f"{fahrenheit}°F = {FparaK(fahrenheit)}K")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao.lower() == "s":
            break
        
        else:
            print("-"*60)
            print("Comando inválido")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue

main()

