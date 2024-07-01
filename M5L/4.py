# Um armazém trabalha com um determinado número de mercadorias diferentes (um
# máximo de 100 itens). Faça um programa que leia e armazene em vetores os preços
# de cada mercadoria e a quantidade vendida no mês e, além disso, calcule e imprima:
# a. O faturamento mensal do armazém.
# b. A mercadoria mais vendida e a menos vendida.
# c. O preço da mercadoria menos vendida.
# d. Quantas mercadorias têm seu preço mais alto que o preço da mercadoria
# menos vendida.

mercadorias = []
preco = []
vendas = []

n_mercadorias = 0
faturamento = 0
mais_vendidas = menos_vendidas = 0

while n_mercadorias < 100:
    produto = input("Insira qual é a mercadoria (Insira 0 se não há mais mercadorias): ")
    if produto == "0":
        break
    
    input_preco = input("Insira o preço dessa mercadoria: ")
    input_vendas = input("Insira a quantidade vendida no mês dessa mercadoria: ")

    if input_preco.isalpha() or input_vendas.isalpha():
        print("\nInsira valores numéricos no preço e no número de vendas do produto\n")
    else:
        input_preco = float(input_preco)
        input_vendas = int(input_vendas)

        mercadorias.append(produto)
        preco.append(input_preco)
        vendas.append(input_vendas)

        faturamento += input_preco * input_vendas
        n_mercadorias += 1

for i in vendas:
    if i > mais_vendidas:
        mais_vendidas = i
        index_mais_vendida = vendas.index(i)

    if menos_vendidas == 0 or i < menos_vendidas:
        menos_vendidas = i
        index_menos_vendida = vendas.index(i)

# Identifica qual foi o preço do item menos vendido e o salva em uma variável
preco_menos_vendida = preco[index_menos_vendida]

# Faz uma subtração do número de itens na lista - o (índice do item menos vendido + 1) (que representa a posição dele na lista se ela começasse no 1 ao invés do 0)
preco.sort()
merc_prec_maior = len(preco) - (preco.index(preco_menos_vendida)+1)

print("-"*15)
print("Faturamento mensal do armazém:", faturamento)
print("-"*15)
print("Mercadoria mais vendida: ", mercadorias[index_mais_vendida], "(", vendas[index_mais_vendida], " vendas)", sep="")
print("Mercadoria menos vendida: ", mercadorias[index_menos_vendida], "(", vendas[index_menos_vendida], " vendas)", sep="")
print("-"*15)
print("Preço da mercadoria menos vendida: R$", preco_menos_vendida)
print("-"*15)
print(merc_prec_maior, "mercadorias têm o preço mais alto que a mercadoria menos vendida")
print("-"*15)