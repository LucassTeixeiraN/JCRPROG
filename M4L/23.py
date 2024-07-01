# Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário
# aos espectadores, no qual constava a idade e a sua opinião em relação ao filme,
# segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo
# estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule
# e imprima:
# a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo.
# b. A percentagem de ótimo, bom, regular, ruim e péssimo.
# c. A idade do mais velho entrevistado.
# d. A idade do mais novo entrevistado.

otimo_resp = bom_resp = regular_resp = ruim_resp = pessimo_resp = 0
mais_velho = mais_novo = 0
lugares = 0

while lugares < 50:
    lugares += 1

    nota = int(input("Qual sua opnião em relação ao filme:\n1-Ótimo\n2-Bom\n3-Regular\n4-Ruim\n5-Péssimo\n"))
    idade = int(input("Insira sua idade: "))

    if nota == 1:
        otimo_resp += 1
    elif nota == 2:
        bom_resp += 1
    elif nota == 3:
        regular_resp += 1
    elif nota == 4:
        ruim_resp += 1
    else:
        pessimo_resp += 1

    if idade > mais_velho:
        mais_velho = idade
    
    if mais_novo == 0 or idade < mais_novo:
        mais_novo = idade

print("Opniões:\nÓtimo - ", otimo_resp, " = ", (otimo_resp/lugares)*100, "%", 
      "\nBom - ", bom_resp, " = ", (bom_resp/lugares)*100, "%", 
      "\nRegular - ", regular_resp, " = ", (regular_resp/lugares)*100, "%", 
      "\nRuim - ", ruim_resp, " = ", (ruim_resp/lugares)*100, "%", 
      "\nPéssimo - ", pessimo_resp, " = ", (pessimo_resp/lugares)*100, "%", 
      "\n\nO entrevistado mais velho possui: ", mais_velho, " anos", 
      "\ne o mais novo possui: ", mais_novo, " anos", sep="")
