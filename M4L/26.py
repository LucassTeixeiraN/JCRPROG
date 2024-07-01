# Uma empresa está fazendo um estudo de possibilidades de aumento aos seus
# funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à
# todos os funcionários ou seguir a seguinte tabela progressiva:

#   Salário           Percentual de aumento
# até R$1000,00              15%
# até R$2000,00              10%
# acima de R$2000,00         5%

# Faça um programa que leia o salário de um número qualquer de funcionários,
# imprimindo para cada um o novo salário nos dois casos (aumento uniforme ou
# aumento progressivo). Ao final, o programa deve fornecer:
# a. O total de funcionários
# b. O salário médio dos funcionários
# c. O total da folha de pagamentos atual
# d. O total da folha de pagamentos futura nos dois casos estudados, indicando
# qual o caminho mais econômico para a empresa

total_funcionarios = total_salario = soma_salario_uni = soma_salario_prog = 0

while True:

    salario = float(input("Insira o salário do funcionário (se não houver mais funcionários digite 0): "))


    if salario == 0:
        break

    total_funcionarios += 1
    total_salario += salario

    aum_uni = salario * 1.1
    soma_salario_uni += aum_uni

    if salario <= 1000:
        aum_prog = salario * 1.15
    elif salario <= 2000:
        aum_prog = salario * 1.1
    else:
        aum_prog = salario * 1.05

    soma_salario_prog += aum_prog

    print("Aumento uniforme: ", aum_uni, "\nAumento progressivo: ", aum_prog, sep="")


salario_medio = total_salario / total_funcionarios


print("Total de funcionários: ", total_funcionarios, 
      "\nSalário Médio: ", salario_medio, 
      "\nTotal da folha de pagamento atual: ", total_salario, 
      "\nFolha de pagamento futura:\nAumento uniforme: ", soma_salario_uni, 
      "\nAumento progressivo: ", soma_salario_prog, sep="")


if soma_salario_uni < soma_salario_prog:
    print("Portanto, o aumento uniforme é mais vantajoso para a empresa.")
else:
    print("Portanto, o aumento progressivo é mais vantajoso para a empresa.")