'''Escreva uma função que, dada uma lista bidimensional (lista de listas), verifique
se ela é uma matriz. Em caso positivo, sua função deve retornar uma tupla com o
número de linhas e de colunas da matriz. Em caso negativo, deve retornar uma
tupla vazia.'''

def criarLista():
    lista = []

    print("Insira uma lista bidimensional colocando espaços entre os elementos de uma linha e apertando ENTER entre cada linha")
    print("Obs: Deixe a linha vazia quando não houver mais elementos a serem lidos")
    while True:
        try:
            linha = input()
            if linha == "":
                break
            valor = [int(numero) for numero in linha.split()]

            lista.append(valor)
        except ValueError:
            print("Valor inválido")
            
    return lista

def analiseMatriz():

    lista = criarLista()
    n_colunas = len(lista[0])
    matriz = True

    for i in lista:
        if len(i) != n_colunas:
            matriz = False
            break
        
    if matriz == True:
        print((len(lista), n_colunas))
    else:
        print(())

    print("-"*60)

def main():
    analiseMatriz()
    
main()
