# 15. Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se cada lista em w tiver igual número de
# elementos positivos e negativos, e False em caso contrário. Por exemplo, no caso da
# lista [[2,4,-3,-1],[-3,0,7],[-8,6]] a função deve devolver True pois todas as listas têm
# igual número de elementos positivos e negativos.


def conta_pos_neg(lista):
   
    pos = 0 
    neg = 0
    for num in lista:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    return pos, neg

def verifica_pos_neg_igual(lista_de_listas):
   
    if not lista_de_listas:
        return True

    for lista in lista_de_listas[1:]:
        pos_lista, neg_lista = conta_pos_neg(lista)
        if pos_lista != neg_lista:
            return False

   
    return verifica_pos_neg_igual(lista_de_listas[1:])

def main():
    entrada_usuario = input("Digite uma lista de listas de números inteiros (separe os elementos por vírgula e use ponto e virgula para separar as sublistas): ")
    try:
    
        lista_de_listas = [list(map(int, sublist.split(','))) for sublist in entrada_usuario.split(';')]
        resultado = verifica_pos_neg_igual(lista_de_listas)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros separados por vírgula e listas separadas por ponto e vírgula.")
main()
