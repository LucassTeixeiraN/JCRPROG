'''Escreva uma função que, dada uma lista bidimensional (lista de listas), verifique
se ela é uma matriz. Em caso positivo, sua função deve retornar uma tupla com o
número de linhas e de colunas da matriz. Em caso negativo, deve retornar uma
tupla vazia.'''

def criarLista():
    lista = []

    print("Insira uma lista bidimensional colocando espaços entre os elementos de uma linha e apertando ENTER entre cada linha")
    print("Obs: Deixe a linha vazia quando não houver mais elementos a serem lidos")
    while True:
        linha = []

        valor = input()
        if valor == "":
            break
        
        valor_listado = valor.split()
        for i in valor_listado:
            linha.append(i)

        lista.append(linha)
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

def main():
    analiseMatriz()
    
main()

#rever linha 18
#Formatação output
#verificação
