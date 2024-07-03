'''
Faça um programa que encontre todas as chaves que estão associadas a um
determinado valor em um dicionário. O programa deve preencher um dicionário pelo
usuário e, a partir desse dicionário e de um valor indicado pelo usuário, encontrar e
exibir as chaves relacionadas ao valor em forma de lista.
'''

dic = {}
lista_chaves = []

print("Insira uma chave e logo em seguida o valor relacionado a ela, deixe a chave em branco quando não houver mais elementos a serem adicionados (pressione ENTER entre a chave o valor)")
n = int(input("Digite quantas chaves ira colocar: "))
for i in range(n):
    chave = input(f"Digite a chave do {i+1}° elemento: ")
    if chave == "":
        break
    valor = input(f"Digite o valor do {i+1}° elemento: ")

    dic[chave] = valor

valor_indicado = input("Insira um valor para saber quais chaves estão relacionadas a ele: ")

for (chave, valor) in dic.items():
    if valor == valor_indicado:
        lista_chaves.append(chave)

if len(lista_chaves) != 0:
    print(lista_chaves)
else:
    print("Não há chaves relacionadas a esse valor")