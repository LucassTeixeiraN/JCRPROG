# 15. Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se cada lista em w tiver igual número de
# elementos positivos e negativos, e False em caso contrário. Por exemplo, no caso da
# lista [[2,4,-3,-1],[-3,0,7],[-8,6]] a função deve devolver True pois todas as listas têm
# igual número de elementos positivos e negativos.

def conta_pos_neg(lista, pos = 0, neg = 0):

    if len(lista) < 1:
        return pos, neg
    elif lista[0] > 0:
        return conta_pos_neg(lista[1:], pos + 1, neg)
    elif lista[0] < 0:
        return conta_pos_neg(lista[1:], pos, neg + 1)
    else:
        return conta_pos_neg(lista[1:], pos, neg)

def verifica_pos_neg_igual(lista):

    if not lista:
        return True
        
    pos, neg = conta_pos_neg(lista[0])
    
    if pos == neg:
        return verifica_pos_neg_igual(lista[1:])
    else:
        return False


def main():
    entrada_usuario = input("Digite uma lista de listas de números inteiros (separe os elementos por vírgula e use ponto e virgula para separar as sublistas): ")
    try:
    
        lista_de_listas = [list(map(int, sublist.split(','))) for sublist in entrada_usuario.split(';')]
        resultado = verifica_pos_neg_igual(lista_de_listas)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros separados por vírgula e listas separadas por ponto e vírgula.")
main()
