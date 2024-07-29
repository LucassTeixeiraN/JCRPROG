# 9. Usando algoritmos recursivos, escreva funções que:
# a. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos n primeiros quadrados perfeitos.
# b. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos quadrados perfeitos até n, por ordem decrescente.



def quad_perf(n):
    """Retorna uma lista dos primeiros n quadrados perfeitos."""
    if n <= 0:
        return []  
    return [i**2 for i in range(1, n + 1)]

def quad_perf_inv(n):
    """Retorna uma lista dos quadrados perfeitos até n, em ordem decrescente."""
    quadrados = []
    i = 1
    while i * i <= n:
        quadrados.append(i * i)
        i += 1
    return sorted(quadrados, reverse=True)

def main():
    while True:
        print("\nMenu:")
        print("1. Lista dos primeiros n quadrados perfeitos")
        print("2. Lista dos quadrados perfeitos até n (em ordem decrescente)")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        try:
            if escolha == '1':
                n = int(input("Insira um número para obter a lista dos primeiros n quadrados perfeitos: "))
                if n > 0:
                    print(quad_perf(n))
                else:
                    print("O número deve ser maior que zero.")
            elif escolha == '2':
                n = int(input("Insira um número para obter a lista dos quadrados perfeitos até n (em ordem decrescente): "))
                if n > 0:
                    print(quad_perf_inv(n))
                else:
                    print("O número deve ser maior que zero.")
            elif escolha == '0':
                print("Saindo")
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Valor invalido")


main()

