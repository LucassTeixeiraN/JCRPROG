'''Escreva um programa com uma função para receber do usuário um conjunto de
valores reais e também com funções próprias que recebem como argumento uma
lista e calculem e retornem a média, o maior, o menor e a soma dos elementos da
lista'''

# Função principal para executar o programa
def main():
    lista = criarLista()  # Cria a lista com valores reais fornecidos pelo usuário
    
    print("-"*60)
    media(lista)  # Calcula e exibe a média dos valores da lista
    maiorN(lista)  # Encontra e exibe o maior valor da lista
    menorN(lista)  # Encontra e exibe o menor valor da lista
    somaLista(lista)  # Calcula e exibe a soma dos valores da lista
    print("-"*60)

# Função para criar uma lista com valores reais fornecidos pelo usuário
def criarLista():
    lista = []

    print("Insira valores reais para compor uma lista. (Deixe em branco caso não deseje adicionar mais valores)")
    while True:
        valor = input()

        if valor == "":  # Encerra a entrada de valores se o usuário deixar em branco
            break
        
        if not valor.isalpha():  # Verifica se a entrada não é alfabética
            lista.append(float(valor))  # Adiciona o valor convertido para float à lista
    return lista

# Função para calcular e exibir a média dos valores da lista
def media(list):
    media = sum(list) / len(list)  # Calcula a média
    print(f"A média dos valores da lista é {media:.2f}")

# Função para encontrar e exibir o maior valor da lista
def maiorN(list):
    maior_n = 0

    for i in list:
        if i > maior_n:
            maior_n = i

    print(f"O maior valor da lista é {maior_n}")

# Função para encontrar e exibir o menor valor da lista
def menorN(list):
    menor_n = 0

    for i in list:
        if i < menor_n or menor_n == 0:
            menor_n = i

    print(f"O menor valor da lista é {menor_n}")

# Função para calcular e exibir a soma dos valores da lista
def somaLista(list):
    soma = sum(list)  # Calcula a soma

    print(f"A soma dos elementos da lista é {soma}")

# Chama a função principal se o script for executado diretamente
main()

