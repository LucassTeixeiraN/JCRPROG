#5. Implemente um programa com uma função que, dada uma lista, retorne outra lista,
#com os elementos da lista original, sem repetições.



def remove_repetidos(lista):
    lista_sem_repetidos = []
    for elemento in lista:
        if elemento not in lista_sem_repetidos:
            lista_sem_repetidos.append(elemento)
    return lista_sem_repetidos

# Solicita ao usuário a quantidade de números e verifica se é um número válido
while True:
    try:
        quantidade = int(input("Quantos números você deseja inserir? "))
        break
    except ValueError:
        print("Por favor, insira um número válido.")

# Solicita os números e verifica se são válidos
numeros = []
for i in range(quantidade):
    while True:
        try:
            numero = int(input("Digite um número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, insira um número válido.")

# Chama a função e imprime a lista sem repetições
lista_sem_repetidos = remove_repetidos(numeros)
print("Lista sem repetições:", lista_sem_repetidos)




