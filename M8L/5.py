# algoritmo de euclides para calcular MDC
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para calcular o MMC entre dois números , utilizando o algoritmo de euclides
def mmc(a, b):
    return (a * b) // mdc(a, b)

# Função para calcular o MMC de uma lista de números
def mmc_lista(numeros):
    if len(numeros) < 2:
        return None  # Lista deve ter pelo menos dois números
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mmc(resultado, num)
    return resultado

def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def main():
    while True:
        a = obter_inteiro("Digite o primeiro número: ")
        b = obter_inteiro("Digite o segundo número: ")
        print(f"O MMC de {a} e {b} é: {mmc(a, b)}")

        # Entrada de uma lista de números para calcular o MMC
        while True:
            try:
                numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
                break
            except ValueError:
                print("Por favor, insira apenas números inteiros separados por espaço.")
        
        print(f"O MMC da lista {numeros} é: {mmc_lista(numeros)}")
        break
if __name__ == "__main__":
    main()
