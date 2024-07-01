# Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte
# forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for
# da categoria “Gerente”, receberá 20% de aumento e os demais funcionários
# receberão 15% de aumento. Faça um programa utilizando o comando if else aninhado
# que leia do teclado o salário e a categoria do funcionário, calcule e imprima o seu
# novo salário. 

salario = int(input("Insira o salário do funcionário: "))
categoria = input("Insira a categoria do funcionário: ")

if categoria == "técnico":
    print("O novo salário desse funcionário é R$ ", salario*1.3)
elif categoria == "gerente":
    print("O novo salário desse funcionário é R$ ", salario*1.2)
else:
    print("O novo salário desse funcionário é R$ ", salario*1.15)
