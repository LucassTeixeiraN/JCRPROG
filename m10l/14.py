'''14. Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se todas as listas em w verificam a propriedade de
mais de metade dos seus elementos serem 0 e False em caso contrário. Por exemplo,
no caso da lista [[0,0,3,0],[0,5,0],[0,0,0]] a função deve devolver True pois em todas as
listas mais de metade dos elementos são 0.
'''

def contar_pares(lista):
    
    if not lista:
        return True

    primeira_sublista = lista[0]
    restantes_listas = lista[1:]

    # Calcular a quantidade de zeros na primeira sublista
    qnt_0 = sum(1 for x in primeira_sublista if x == 0)
    metade = len(primeira_sublista) / 2
        
    # Verifica se o número de zeros é maior que a metade do comprimento da sublista
    if qnt_0 > metade:
        return contar_pares(restantes_listas)
    else:
        return False
            
    
   
    
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
        
