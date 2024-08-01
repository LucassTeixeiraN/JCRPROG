# Usando algoritmos recursivos, escreva funções que:
# a. Obtenha o máximo de uma lista.
# b. Obtenha o máximo de uma lista com n números.
# c. Buscar um caractere c em uma string s a partir de uma posição index e retornar a
# posição da primeira ocorrência deste caractere (caso encontre) ou −1 (caso
# contrário).


def maximoLista(lista, max = 0, indice = 0):
    if indice < len(lista):
        if max == 0 or lista[indice] > max:
            max = lista[indice]
            
        return maximoLista(lista, max, indice+1)
    return max

def listaNNumeros(n, lista, max = 0):
    if n >= 0:
        if max == 0 or lista[n] > max:
            max = lista[n]

        return listaNNumeros(n-1, lista, max)
    return max

def buscarCaracter(string, carac, indice = 0):
    if indice < len(string):
        if string[indice] == carac:
            return indice
        return buscarCaracter(string, carac, indice+1)
    return -1

def menu():
    print("-"*60)
    print("Selecione uma das seguintes opções:")
    print("1 - Obtenha o máximo de uma lista.")
    print("2 - Obtenha o máximo de uma lista com n números.")
    print("3 - Buscar um caractere c em uma string s a partir de uma posição index e retornar a posição da primeira ocorrência deste caractere (caso encontre) ou −1 (caso contrário).")
    print("0 - Sair do programa.")
    opcao = input()
    print("-"*60)
    return opcao

def main():

    while True:
        opcoes = menu()

        try:
            if opcoes == "1":
                print("Insira números para uma lista (utilize espaço entre cada número e pressione ENTER quando não houver mais elementos): ")
                lista = [int(num) for num in input().split()]
                print(f"O máximo da lista inserida é: {maximoLista(lista)}")

            elif opcoes == "2":
                n = int(input("Insira o número de elementos de sua lista: "))
                lista = []
                print("Insira os elementos de sua lista apertando ENTER entre cada um: ")
                for i in range(n):
                    lista.append(int(input()))
                print(f"O máximo da lista inserida é: {listaNNumeros(n-1, lista)}")

            elif opcoes == "3":
                s = input("Insira uma palavra: ")
                c = input("Insira um caractere para ser buscado na palavra anterior: ")
                print(f"O caractere {c} está no index: {buscarCaracter(s, c)}")

            elif opcoes == "0":
                print("Finalizando programa")
                print("-"*60)
                break
            
            else:
                print("Insira uma opção válida")
        except ValueError:
            print("Valor inválido")

main()
