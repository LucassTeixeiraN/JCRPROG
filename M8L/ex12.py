'''O valor aproximado de pi pode ser calculado a partir da série: 𝜋 = 4/1 - 4/3 + 4/5 - 4/7 + ⋯
Escreva uma função que calcule o valor de , com precisão dada como parâmetro. '''

def calcular_pi(precisao):
    '''
    A precisão determina quantos termos da série serão usados.
    Quanto maior a precisão, mais próximo do valor real de π será o resultado.
    '''
    pi_aproximado = 0
    sinal = 1

    for i in range(1, precisao + 1):
        termo = 4 / (2 * i - 1) # Usado para determinar o denominador
        pi_aproximado += sinal * termo 
        sinal *= -1 # Multiplica ele mesmo por -1 para que altere o sinal entre + e -, quando o sinal for 1 sera positivo, entao * -1, ficara negativo.

    return pi_aproximado

def main():
# Exemplo de uso:
    while True:
        try:
            precisao_desejada = input("Insira a precisao desejada (Obs: Insira números inteiros e pressione ENTER para sair do programa): ")  # Aumenta a precisão para obter um resultado mais próximo de pi (numero de termos de pi)
            if precisao_desejada == "":
                print("\nPrograma encerrado")
                break
            precisao_desejada = int(precisao_desejada)
            valor_pi = calcular_pi(precisao_desejada)
            print(f"Valor aproximado de π com {precisao_desejada} termos: {valor_pi:.10f}")
            
        except ValueError:
            print("insira um número valído!")
        
main()
