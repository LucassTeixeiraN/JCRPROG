# Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
# número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
# quantidade vendida. A partir desses dados imprima: o número total de mercadorias
# diferentes lidas, o faturamento total e o lucro total do armazém. 

total_mercadoria = faturamento_total = custo_total = lucro_total = 0

while True:

    x = input("informe a mercadoria: ")
    custo = int(input("informe o preço de custo de " + x + ":"))
    venda = int(input("informe o preço de venda de " + x + ":"))
    qntdd = int(input("informe a quantidade vendida de " + x + ":"))

    FIM = int(input("Você deseja adicionar mais mercadorias? \n1- Sim\n2- Não\n"))

    custo_total += custo * qntdd
    total_mercadoria += 1
    faturamento_total += venda * qntdd
    
    if FIM == 2:
        break

lucro_total += faturamento_total - custo_total

print("Teve um total de",total_mercadoria, "mercadorias diferentes\nHouve faturamento total de R$" ,faturamento_total, "\nE um lucro de R$",lucro_total)
