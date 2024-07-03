'''Escreva um programa que receba um dicionário d e retorna um dicionário “inverso”
do dicionário dado, onde, a cada valor v de d está associada a lista das chaves de d
que levam a v.'''

dic = {}
dic_inv = {}

print("-"*70)
print("Deixe a chave em branco se não houver mais itens a serem adicionados")
i = 1
while True:
    chave = input(f"Insira o valor da {i}° chave: ")
    if chave == "":
        break

    valor = input(f"Insira o valor do {i}° valor: ")

    dic[chave] = valor
    i += 1

for (chave, valor) in dic.items():
    lista = []
    if not valor in dic_inv:
        lista.append(chave)
        dic_inv[valor] = lista
    else:
        dic_inv[valor].append(chave)

print(dic_inv)
print("-"*70)
