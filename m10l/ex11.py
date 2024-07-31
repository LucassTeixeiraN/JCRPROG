'''11. Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve o número de elementos pares que existem nas
sublistas de w. Por exemplo, no caso da lista [[2,4,3,1],[3,5,7],[],[8,0,6]] a função deve
devolver 5.'''


def contar_pares(lista):
    
    if not lista:
        return 0
    
    primeira_sublista = lista[0]
    restantes_listas = lista[1:]
    
    pares_na_primeira = sum(1 for x in primeira_sublista if x % 2 == 0 and x != str(x))
    
    pares_nas_restantes = contar_pares(restantes_listas)
    
   
    return pares_na_primeira + pares_nas_restantes
def main():
    print("Digite uma sequencia de numeros e aperte ENTER para serem colocados em um subconjunto:")
    lista_principal = []
    while True:
      
        entrada  = input()
        
        if entrada.lower() == "exit":
            break
       
        try:
            subsequencia = list(map(int, entrada.split()))
            lista_principal.append(subsequencia)
        except ValueError:
            print('Entrada inválida, apenas números são permitidos.')

    return lista_principal

print(contar_pares(main()))       
        
   
