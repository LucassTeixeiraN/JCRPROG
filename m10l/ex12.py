'''
Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se em todas as sublistas de w existir um número
positivo. Por exemplo, no caso da lista [[2,4,3,1],[3,-5,-7],[],[8,0,-6]] a função deve
devolver False porque em [] não existe nenhum número positivo
'''
def numPositivo(sublista):
    for num in sublista:
        if num > 0:
            return True
    return False

def listaTotal(listas):
    if not listas:
        return True
    else:
        primeiraSub = listas[0]
        restante = listas[1:]
        return numPositivo(primeiraSub) and listaTotal(restante)

def main():
    while True:
        try:
            w = []
            n_listas = int(input("\nInsira o número de listas dentro da lista: "))
            print("\nInsira as listas deixando espaço entre os elementos e pressionando ENTER entre cada lista")
            for i in range(n_listas):
                lista = [int(num) for num in input().split()]
                w.append(lista)
            print("-"*50)
            print(f"Lista: {w} \nResultado: {listaTotal(w)}")
            print("-"*50)
            break
        except ValueError:
            print("\nValor inválido. Certifique-se de inserir sempre apenas numeros inteiros.")
main()
