# Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
# mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
# ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:

# Tipo            Quantidade          vendida Comissões
# 8 K             10 ou mais         R$ 550 por TV vendida
#                Menos que 10        R$ 350 por TV vendida
# 4 K            10 ou mais          R$ 420 por TV vendida
#               Menos que 10         R$ 250 por TV vendida

# Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
# INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de
# 5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
# vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
# com os descontos). Além disso, no final, o programa deve:
# a. Imprimir o número de funcionários.
# b. Imprimir o total de salários pagos.
# c. Imprimir a média das comissões.
# d. Imprimir o valor da maior e da menor comissão paga pelo departamento. 

numero_funcionarios = salario_soma = comissao_soma = menor_comissao = maior_comissao = 0

while True:
    salario = int(input("Insira o salário do funcionário (digite -1 se não há mais funcionário) "))
    if salario == -1:
        break

    tv8k = int(input("Insira o número de televisores 8k vendidos pelo funcionário "))
    tv4k = int(input("Insira o número de televisores 4k vendidos pelo funcionário "))

    comissao = 0
    numero_funcionarios += 1

    if tv8k >= 10:
        salario += 550*tv8k
        comissao_soma += 550*tv8k
        comissao += 550*tv8k
    else:
        salario += 350*tv8k
        comissao_soma += 350*tv8k
        comissao += 350*tv8k

    if tv4k >= 10:
        salario += 420*tv4k
        comissao_soma += 420*tv4k
        comissao += 420*tv4k
    else:
        salario += 250*tv4k
        comissao_soma += 250*tv4k
        comissao += 250*tv4k
    
    if menor_comissao == 0 or comissao < menor_comissao:
        menor_comissao = comissao

    if comissao > maior_comissao:
        maior_comissao = comissao


    if salario > 950:
        salario_liquido = salario * 0.92 * 0.95
    else:
        salario_liquido = salario * 0.92

    salario_soma += salario_liquido

    print("O funcionário receberá R$", salario_liquido)

comissao_media = comissao_soma / numero_funcionarios

print("Total de funcionários: ", numero_funcionarios, 
      "\nSoma dos salários: R$", salario_soma, 
      "\nMédia das comissões: R$", comissao_media, 
      "\nMaior comissão: R$", maior_comissao, 
      "\nMenor Comissão: R$", menor_comissao, sep="")