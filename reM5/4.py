# Um armazém trabalha com um determinado número de mercadorias diferentes (um
# máximo de 100 itens). Faça um programa que leia e armazene em vetores os preços
# de cada mercadoria e a quantidade vendida no mês e, além disso, calcule e imprima:
# a. O faturamento mensal do armazém.
# b. A mercadoria mais vendida e a menos vendida.
# c. O preço da mercadoria menos vendida.
# d. Quantas mercadorias têm seu preço mais alto que o preço da mercadoria
# menos vendida.

MAX_ITENS = 100
produtos = []
precos = []
qnt_vendida = []

faturamento_total = 0
mais_vendida = menos_vendida = 0
mercadorias_mais_caras = 0

i = 0
while i < MAX_ITENS:
    produto = input("Insira o nome do produto (deixe em branco caso não haja mais produtos a serem adicionados): ")
    if produto == "":
        break

    preco = input(f"Insira o preço do produto {produto}: ")
    vendas = input(f"Insira o número de vendas do produto {produto}: ")

    if not produto in produtos and not preco.isalpha() and float(preco) > 0 and vendas.isnumeric() and int(vendas) > 0:
        preco = float(preco)
        vendas = int(vendas)

        produtos.append(produto)
        precos.append(preco)
        qnt_vendida.append(vendas)

        faturamento_total += preco * vendas
        i += 1
    else:
        print("Produto inválido")

# Vai rodar o i no range da quantidade de elementos dentro das listas
for i in range(len(qnt_vendida)):
    if qnt_vendida[i] > mais_vendida:
        mais_vendida = qnt_vendida[i]
        index_mais_vendida = i
    
    if menos_vendida == 0 or qnt_vendida[i] < menos_vendida:
        menos_vendida = qnt_vendida[i]
        index_menos_vendida = i


for i in range(len(precos)):
    if precos[i] > precos[index_menos_vendida]:
        mercadorias_mais_caras += 1


print("-" * 60)
print(f"Faturamento total: R${faturamento_total:.2f}")
print(f"Mercadoria mais vendida: {produtos[index_mais_vendida]}")
print(f"Mercadoria menos vendida: {produtos[index_menos_vendida]}")
print(f"Preço da mercadoria menos vendida: R${precos[index_menos_vendida]:.2f}")
print(f"Número de mercadorias mais caras que a mercadoria menos vendida: {mercadorias_mais_caras}")
print("-" * 60)