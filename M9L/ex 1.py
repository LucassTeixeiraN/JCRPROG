"""Escreva uma função que leia e retorne uma matriz de inteiros fornecida pelo
usuário. Sua matriz deve ler os números linha a linha. Os números devem estar
separados por espaços em branco. Sua função deve interromper a leitura ao
receber uma linha em branco
"""

# Define uma função para ler e retornar uma matriz de inteiros fornecida pelo usuário.
def ler_matriz():
    matriz = []  # Inicializa uma lista vazia para a matriz.
    while True:
        try:
            linha = input("Digite uma linha de números separados por espaços (ou deixe em branco para encerrar): ")
            if not linha:
                break  # Interrompe a leitura se a linha estiver em branco.
            numeros = [int(num) for num in linha.split()]  # Converte os números da linha em uma lista de inteiros.
            matriz.append(numeros)  # Adiciona a lista de números à matriz.
        except ValueError:
            print("Por favor, insira apenas números inteiros separados por espaços.")
    return matriz

def main():
    minha_matriz = ler_matriz()  # Chama a função para ler a matriz.
    print("-" * 60)
    print("Matriz lida:")
    for linha in minha_matriz:
        print(linha)  # Imprime cada linha da matriz.
    print("-" * 60)
main()
