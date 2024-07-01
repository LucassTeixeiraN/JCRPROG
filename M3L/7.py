# Um microempresário tem por norma retirar mensalmente 40% do lucro de sua
# empresa para os seus gastos pessoais se o lucro ultrapassar R$ 3.000,00 e retirar
# apenas R$ 1.000,00 se o lucro for menor que isso. Faça um programa que leia do
# teclado o faturamento mensal e o total das despesas para calcular o lucro (lucro =
# faturamento - despesas) e imprima quanto o microempresário deve retirar neste mês.
# Declare como constantes simbólicas o lucro mínimo, a retirada mínima e o limite da
# retirada

lucro_min = retirada_min = 1000
retirada_limite = 0.4

faturamento = float(input("Insira o faturamento da empresa: "))
despesa = float(input("Insira as despesas da empresa: "))

lucro = faturamento - despesa

if lucro < lucro_min:
    print("Não houve lucro suficiente para a retirada")
elif (lucro > lucro_min) & (lucro <= 3000):
    print("Deve ser retirado R$", retirada_min)
else:
    print("Deve ser retirado R$", lucro*retirada_limite)