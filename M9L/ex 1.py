
"""Escreva uma função que leia e retorne uma matriz de inteiros fornecida pelo
usuário. Sua matriz deve ler os números linha a linha. Os números devem estar
separados por espaços em branco. Sua função deve interromper a leitura ao
receber uma linha em branco
"""


def ler_matriz():
    matriz = []
    while True:
        try:
            linha = input("Digite uma linha de números separados por espaços (ou deixe em branco para encerrar): ")
            if not linha:
                break
            numeros = [int(num) for num in linha.split()]
            matriz.append(numeros)
        except ValueError:
            print("Por favor, insira apenas números inteiros separados por espaços.")
    return matriz

def main():
    minha_matriz = ler_matriz()
    print("Matriz lida:")
    for linha in minha_matriz:
        print(linha)
main()