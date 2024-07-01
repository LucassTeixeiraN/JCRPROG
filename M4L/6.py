# Alterar o programa anterior para só contar caracteres diferentes de espaço em branco
# e tabulação
input = list(input("Insira um texto para descobrir quantos caracteres ele possui:\n"))
numero_caracteres = 0

for i in input:
    if i != " " and i != "\t":
        numero_caracteres += 1

print(numero_caracteres)