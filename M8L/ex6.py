'''6. Crie um programa que implemente uma função que, dada uma lista, retorne a moda
da lista, ou seja, uma lista com o(s) elemento(s) mais frequente(s) da lista original.'''
def moda(lista):
            
    frequencia = {}
            
    for elemento in lista:
        if elemento in frequencia:
            frequencia[elemento] += 1
        else:
            frequencia[elemento] = 1
            
    max_freq = max(frequencia.values())
        
    result = []
        
    for elemento, freq in frequencia.items():
        if freq == max_freq:
            result.append(elemento)
            
    return result
print(f"Digite o numero e aperte ENTER: \ncaso queira parar digite S:")

def main():
    lista=[]
    while True:
        x = input()
        if x.isnumeric():
            lista.append(int(x))
        elif x.upper() == "S":
            print(f"Lista original: {lista}")
            print(f'Moda(s): {moda(lista)}')
            break
        else:
            print("Entrada invalida")
            print("Digite novamente:")    
main()
        
