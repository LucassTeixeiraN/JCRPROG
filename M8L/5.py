#5. Implemente um programa com uma função que, dada uma lista, retorne outra lista,
#com os elementos da lista original, sem repetições.



def remove_repetidos(lista):
    lista_sem_repetidos = []
    for elemento in lista:
        if elemento not in lista_sem_repetidos:
            lista_sem_repetidos.append(elemento)
    return lista_sem_repetidos

def main():
    numeros = []
    while True:
        try:
            entrada = input("Digite um número (ou pressione Enter para encerrar): ")
            if entrada == "":
                break
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")

    lista_sem_repetidos = remove_repetidos(numeros)
    print("Lista sem repetições:", lista_sem_repetidos)

main()
