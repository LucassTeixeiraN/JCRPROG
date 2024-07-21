'''O valor aproximado de pi pode ser calculado a partir da série: 𝜋 = 4/1 - 4/3 + 4/5 - 4/7 + ⋯
Escreva uma função que calcule o valor de , com precisão dada como parâmetro. '''

# Função para calcular o valor aproximado de π usando a série de Leibniz
def calcular_pi(precisao):
    '''
    A precisão determina quantos termos da série serão usados.
    Quanto maior a precisão, mais próximo do valor real de π será o resultado.
    '''
    pi_aproximado = 0
    sinal = 1

    for i in range(1, precisao + 1):
        termo = 4 / (2 * i - 1)  # Usado para determinar o denominador
        pi_aproximado += sinal * termo  # Adiciona ou subtrai o termo da série
        sinal *= -1  # Alterna o sinal entre + e -

    return pi_aproximado  # Retorna o valor aproximado de π

# Função principal para obter a entrada do usuário e calcular π
def main():
    # Exemplo de uso:
    while True:
        try:
            precisao_desejada = input("Insira a precisao desejada (Obs: Insira números inteiros e pressione ENTER para sair do programa): ")  # Solicita a precisão desejada
            if precisao_desejada == "":
                print("\nPrograma encerrado")
                break
            precisao_desejada = int(precisao_desejada)  # Converte a entrada para um número inteiro
            valor_pi = calcular_pi(precisao_desejada)  # Calcula o valor aproximado de π
            print(f"Valor aproximado de π com {precisao_desejada} termos: {valor_pi:.10f}")  # Exibe o valor aproximado de π
            
        except ValueError:
            print("insira um número valído!")  # Mensagem de erro para entradas não inteiras

# Chama a função principal se o script for executado diretamente
main()

