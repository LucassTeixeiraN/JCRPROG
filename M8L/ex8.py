'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo: C =5/9*(F-32).
A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

# Função para converter temperatura de Fahrenheit para Celsius
def FparaC(F):
    C = 5/9*(F-32)  # Fórmula de conversão de Fahrenheit para Celsius
    return C

# Função principal para ler a entrada do usuário e exibir a conversão
def main():
    while True:
        try:
            print(70*"-")
            F = input("Digite os graus em °F (Deixe em branco para sair do programa): ")
            if F == "":  # Verifica se o usuário deseja encerrar o programa
                print("\nEncerrado!")
                break
            F = int(F)  # Converte a entrada para um número inteiro
            print(f"\nConversao para graus °C: {FparaC(F):.2f}")  # Exibe a conversão para Celsius
        except ValueError:
            print("\nDados invalidos")  # Mensagem de erro para entradas não inteiras
            print(70*"-")

# Chama a função principal se o script for executado diretamente
main()

