'''Defina a função que recebe como argumento um número inteiro positivo e devolve
True se esse número for um número perfeito e False em caso contrário. Recorde que
um número perfeito é um número natural que é igual à soma de todos os seus
divisores próprios, isto é, a soma de todos os divisores excluindo o próprio número.
Pode, se assim o entender, definir funções auxiliares.'''

# Coleta todos os divisores
def divs(n, i=1):
    if i >= (n // 2) + 1:
        return []

    if n % i == 0:
        return [i] + divs(n, i + 1)
    
    return divs(n, i + 1)

def num_per(n):
    tds_divs = divs(n)
    soma_divisores = sum(tds_divs)
    return soma_divisores == n

def obter_numero_positivo():
    while True:
        try:
            numero = int(input("Digite um número positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    numero = obter_numero_positivo()
    if num_per(numero):
        print(f"{numero} é um número perfeito.")
    else:
        print(f"{numero} não é um número perfeito.")

main()

# para n = 2: 2^1(2^2 − 1) = 6
# para n = 3: 2^2(2^3 − 1) = 28
# para n = 5: 2^4(2^5 − 1) = 496
# para n = 7: 2^6(2^7 − 1) = 8.128
