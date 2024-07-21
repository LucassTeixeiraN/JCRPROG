'''6. Crie um programa que implemente uma função que, dada uma lista, retorne a moda
da lista, ou seja, uma lista com o(s) elemento(s) mais frequente(s) da lista original.'''
# Função para calcular a moda de uma lista
def moda(lista):
    frequencia = {}  # Dicionário para armazenar a frequência de cada elemento
    
    for elemento in lista:  # Itera sobre cada elemento da lista
        if elemento in frequencia:  # Verifica se o elemento já está no dicionário
            frequencia[elemento] += 1  # Incrementa a contagem do elemento
        else:
            frequencia[elemento] = 1  # Adiciona o elemento ao dicionário com contagem 1
            
    max_freq = max(frequencia.values())  # Encontra a frequência máxima na lista
        
    result = []  # Lista para armazenar os elementos com a frequência máxima
        
    for elemento, freq in frequencia.items():  # Itera sobre os itens do dicionário
        if freq == max_freq:  # Verifica se a frequência do elemento é igual à frequência máxima
            result.append(elemento)  # Adiciona o elemento à lista de resultados
            
    return result  # Retorna a lista de elementos mais frequentes

print(f"Digite o numero e aperte ENTER: \ncaso queira parar digite S:")

# Função principal para obter a entrada do usuário e exibir a moda da lista
def main():
    lista = []  # Lista para armazenar os números inseridos pelo usuário
    while True:
        x = input()  # Solicita a entrada do usuário
        if x.isnumeric():  # Verifica se a entrada é um número
            lista.append(int(x))  # Adiciona o número à lista
        elif x.upper() == "S":  # Verifica se o usuário deseja encerrar a entrada
            print(f"Lista original: {lista}")  # Exibe a lista original
            print(f'Moda(s): {moda(lista)}')  # Exibe a moda da lista
            break  # Encerra o loop
        else:
            print("Entrada invalida")  # Mensagem de erro para entradas inválidas
            print("Digite novamente:")  # Solicita nova entrada

# Chama a função principal se o script for executado diretamente
main()

