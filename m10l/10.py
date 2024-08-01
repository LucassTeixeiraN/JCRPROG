# 10. Usando algoritmos recursivos, escreva funções que:
# a. Defina uma função que recebe como argumento uma lista de inteiros e devolva
# o produto dos seus elementos.
# b. Defina uma função que recebe como argumento uma lista de números inteiros
# w e devolve True se w contém um número par e False em caso contrário.
# c. Defina uma função que recebe como argumento uma lista de números inteiros
# w e devolve True se w contém apenas números ímpares e False em caso
# contrário

def criar_lista():
    while True:
        try:
            n = int(input("Digite a quantidade de elementos da sua lista: "))
            lista = []
            for i in range(n):
                valor = int(input(f"Informe o valor do elemento {i + 1}: "))
                lista.append(valor)
            return lista
        except ValueError:
            print("insira um numero inteiro!")

def multiplicar_elementos(lista, index=0):
    if index == len(lista):
        return 1
    return lista[index] * multiplicar_elementos(lista, index + 1)

def contem_parQ(w):
   
    if not w: 
        return False
    elif w[0] % 2 == 0: 
        return True
    else:
        return contem_parQ(w[1:])  
    

def contem_apenas_impares(lista):
    if not lista:  
        return True
    else:
        primeiro_elemento = lista[0]
        if primeiro_elemento % 2 == 1:  
            return contem_apenas_impares(lista[1:])  
        else:
            return False



def menu():
    print("\nEscolha uma opção:")
    print("1. Criar lista")
    print("2. verifica se a lista contem numeros pares")
    print("3. Multiplicar elementos")
    print("4. verifica se há somente numeros impares na lista")
    print("5. Sair")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

def main():
    minha_lista = []
    while True:
        opcao = menu()
        if opcao == '1':
            minha_lista = criar_lista()
        elif opcao == '2':
            print(f"A lista contém ao menos um número par?  {contem_parQ(minha_lista)}")

        elif opcao == '3':
            print(f"Produto dos elementos: {multiplicar_elementos(minha_lista)}")
        elif opcao == '4':
            print(f" Todos os números da lista são impares? {contem_apenas_impares(minha_lista)}")
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
