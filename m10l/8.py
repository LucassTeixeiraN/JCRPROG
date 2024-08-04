

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
