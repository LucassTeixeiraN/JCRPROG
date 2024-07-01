# Em uma loja de eletroeletrônicos, um vendedor que consiga vender mais de R$
# 3.000,00 por mês recebe como comissão 5% do valor vendido. Abaixo disso, ele não
# recebe nenhuma comissão. Faça um programa que leia do teclado o total de vendas
# mensais de um vendedor e imprima se ele tem direito a comissão e, se tiver, de
# quanto. 

venda = float(input("Insira o valor da venda mensal: "))
venda_min = 3000
porc_comissao = 0.05
comissao = venda*porc_comissao

if venda > venda_min:
    print("O vendedor deve receber R$", comissao)
else:
    print("O vendedor não receberá comissão")