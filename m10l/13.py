'''13. Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se alguma das listas em w tiver mais números
pares do que ímpares e False em caso contrário. Por exemplo, no caso da lista
[[2,4,3,1],[3,5,7],[8,1,6]] a função deve devolver True pois a lista [8,1,6] tem mais pares
que ímpares.'''

def contar_pares(lista):
def verificar_pares(lista):
    
    if not lista:
        return False
    
    primeira_sublista = lista[0]
    restantes_listas = lista[1:]
    
    
    pares_na_primeira = sum(1 for x in primeira_sublista if isinstance(x, int) and x % 2 == 0)
    impares_na_primeira = sum(1 for x in primeira_sublista if isinstance(x, int) and x % 2 != 0)
    
    
    if pares_na_primeira > impares_na_primeira:
        return True
    
    
    return verificar_pares(restantes_listas)

def main():
    print("Digite uma sequência de números e aperte ENTER para serem colocados em um subconjunto (digite 'exit' para encerrar):")
    print("Numeros negativos serao convertidos para inteiros.")
    print(50*"-")
    lista_principal = []
    while True:
        entrada = input()
        if entrada.lower() == "exit":
            break
       
        try:
            subsequencia =  [int(num) for num in entrada.split()]

            lista_principal.append(subsequencia)
        except ValueError:
            print('Entrada inválida, digite novamente')

    
    resultado = verificar_pares(lista_principal)
    print(resultado)


main()

