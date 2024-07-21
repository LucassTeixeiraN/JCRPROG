'''Escreva uma função que, dada uma lista bidimensional (lista de listas), verifique
se ela é uma matriz. Em caso positivo, sua função deve retornar uma tupla com o
número de linhas e de colunas da matriz. Em caso negativo, deve retornar uma
tupla vazia.'''

def criarLista():
    lista = []  # Inicializa uma lista vazia para a matriz

    print("Insira uma lista bidimensional colocando espaços entre os elementos de uma linha e apertando ENTER entre cada linha")
    print("Obs: Deixe a linha vazia quando não houver mais elementos a serem lidos")
    while True:
        try:
            linha = input()  # Lê uma linha de entrada do usuário
            if linha == "":
                break  # Encerra a entrada quando o usuário insere uma linha vazia
            valor = [int(numero) for numero in linha.split()]  # Converte os valores da linha para inteiros

            lista.append(valor)  # Adiciona a linha à matriz
        except ValueError:
            print("Valor inválido")  # Exibe uma mensagem de erro se o usuário inserir um valor inválido

    return lista

def analiseMatriz():
    lista = criarLista()  # Obtém a matriz criada pelo usuário
    n_colunas = len(lista[0])  # Obtém o número de colunas da primeira linha

    for i in lista:
        if len(i) != n_colunas:
            return ()  # Retorna uma tupla vazia se as linhas tiverem diferentes números de colunas

    return (len(lista), n_colunas)  # Retorna uma tupla com o número de linhas e colunas da matriz

def main():
    analise = analiseMatriz()  # Realiza a análise da matriz
    print(analise)  # Imprime o resultado da análise
    print("-" * 60)  # Exibe uma linha de traços para separar a saída

main()
