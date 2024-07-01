# Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que
# os dados de cada contribuinte (número do CPF, número de dependentes e renda
# mensal) são valores fornecidos pelo usuário. Para cada contribuinte será feito um
# desconto no imposto de 5% do salário mínimo (R$136,00) para cada dependente (o
# salário mínimo e o desconto são designados por constantes simbólicas). Os valores
# da alíquota para cálculo do imposto são:

# Renda Líquida(R$)     Alíquota
#   até 900,00           isento
# 900,01 até 1500,00       5%
# 1500,01 até 1900,00      10%
# 1900,01 até 2200,00      15%
#  acima de 2200,01        20%

# O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final,
# devem ser impressos:
# a. Para cada contribuinte, o total a pagar.
# b. O número de contribuintes.
# c. O total de contribuintes isentos e não isentos.
# d. O total de impostos que serão arrecadados desse grupo de contribuintes.
# e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar
# o maior imposto.



salario_minimo = 136
desconto_pctg = 0.05

n_contribuintes = isentos = nao_isentos = total_impostos = maior_imposto = maior_imposto_cpf = 0

while True:

    cpf = int(input("Insira o CPF do contribuinte (digite 0 se não há mais contribuintes): "))
    if cpf == 0:
        break

    n_dependentes = int(input("Insira o número de dependentes do contribuinte: "))
    renda = int(input("Insira a renda mensal do contribuinte: "))

    n_contribuintes += 1

    if n_dependentes != 0:
        desconto = n_dependentes * salario_minimo * desconto_pctg
    else:
        desconto = 1


    if renda <= 900:
        print("O contribuinte está isento de impostos")
        isentos += 1
    elif renda <= 1500:
        imposto = renda * 0.05 * desconto

        print("O contribuinte irá pagar " + str(imposto) + " de impostos")
        total_impostos += imposto
        nao_isentos += 1

        if maior_imposto < imposto:
            maior_imposto = imposto
            maior_imposto_cpf = cpf

    elif renda <= 1900:
        imposto = renda * 0.1 * desconto

        print("O contribuinte irá pagar " + str(imposto) + " de impostos")
        total_impostos += imposto
        nao_isentos += 1

        if maior_imposto < imposto:
            maior_imposto = imposto
            maior_imposto_cpf = cpf

    elif renda <= 2200:
        imposto = renda * 0.15 * desconto

        print("O contribuinte irá pagar " + str(imposto) + " de impostos")
        total_impostos += imposto
        nao_isentos += 1

        if maior_imposto < imposto:
            maior_imposto = imposto
            maior_imposto_cpf = cpf

    else:
        imposto = renda * 0.2 * desconto

        print("O contribuinte irá pagar " + str(imposto) + " de impostos")
        total_impostos += imposto
        nao_isentos += 1

        if maior_imposto < imposto:
            maior_imposto = imposto
            maior_imposto_cpf = cpf
            
    
print("O número total de contribuintes é: " , n_contribuintes, 
      "\nIsentos: ", isentos, 
      "\nNão isentos: ", nao_isentos,
      "\n\nTotal de impostos arrecadados: ", total_impostos, 
      "\n\nO contribuinte que pagou o maior imposto foi o com o CPF: ", maior_imposto_cpf, 
      "\nPagou: ", maior_imposto, sep="")