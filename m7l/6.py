'''
Faça um programa que encontre todas as chaves que estão associadas a um
determinado valor em um dicionário. O programa deve preencher um dicionário pelo
usuário e, a partir desse dicionário e de um valor indicado pelo usuário, encontrar e
exibir as chaves relacionadas ao valor em forma de lista.
'''

dic = {}

print("Insira uma chave e logo em seguida o valor relacionado a ela, deixe a chave em branco quando não houver mais elementos a serem adicionados (pressione ENTER entre a chave o valor)")
while True:
    chave = input()
    if chave == "":
        break
    valor = input()


    dic[chave] = valor

valor_indicado = input("Insira um valor para saber quais chaves estão relacionadas a ele: ")
lista_chaves = []

for (chave, valor) in dic.items():
    if valor == valor_indicado:
        lista_chaves.append(chave)

print(lista_chaves)