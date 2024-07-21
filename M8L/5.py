#5. Implemente um programa com uma função que, dada uma lista, retorne outra lista,
#com os elementos da lista original, sem repetições.

# Função para remover elementos repetidos de uma lista
def remove_repetidos(lista):
    lista_sem_repetidos = []  # Lista para armazenar os elementos sem repetições
    for elemento in lista:  # Itera sobre cada elemento da lista original
        if elemento not in lista_sem_repetidos:  # Verifica se o elemento já está na lista sem repetições
            lista_sem_repetidos.append(elemento)  # Adiciona o elemento se não estiver na lista sem repetições
    return lista_sem_repetidos  # Retorna a lista sem elementos repetidos

# Função principal para obter a entrada do usuário e exibir a lista sem repetições
def main():
    numeros = []  # Lista para armazenar os números inseridos pelo usuário
    while True:
        try:
            entrada = input("Digite um número (ou pressione Enter para encerrar): ")  # Solicita a entrada do usuário
            if entrada == "":  # Verifica se o usuário pressionou Enter sem digitar um número
                break  # Encerra o loop se o usuário pressionar Enter
            numero = int(entrada)  # Converte a entrada para um número inteiro
            numeros.append(numero)  # Adiciona o número à lista de números
        except ValueError:
            print("Por favor, insira um número válido.")  # Mensagem de erro para entradas não inteiras

    lista_sem_repetidos = remove_repetidos(numeros)  # Chama a função para remover repetições
    print("Lista sem repetições:", lista_sem_repetidos)  # Exibe a lista sem repetições

# Chama a função principal se o script for executado diretamente
main()
