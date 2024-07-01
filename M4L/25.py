# Foi realizada uma pesquisa de algumas características físicas da população de uma
# certa região, a qual foram coletados os seguintes dados referentes a cada habitante
# para serem analisados:
# • Sexo.
# • Cor dos olhos (azuis, verdes, castanhos).
# • Cor dos cabelos (louros, castanhos, pretos).
# • Idade.
# Faça um programa que determine e escreva:
# a. O total de entrevistados
# b. O total de homens e o total de mulheres entrevistados
# c. A maior e a menor idade do conjunto de habitantes;
# d. A média de idade do conjunto de habitantes;
# e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
# anos inclusive e que tenham olhos verdes e cabelos louros.
# O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.
total_entrevistados = total_h = total_m = maior_idd = menor_idd = soma_idd = indv_ex_total = 0


while True:
    idade = int(input("Insira a idade do entrevistado (digite -1 se não há mais entrevistados):\n"))
    
    if idade == -1:
        break
    
    # c)
    if menor_idd == 0 or idade < menor_idd:
        menor_idd = idade

    
    sexo = int(input("Insira o sexo do entrevistado:\n1- Masculino\n2- Feminino\n"))
    cor_olhos= int(input("Insira a cor dos olhos do entrevistado:\n1- Azuis\n2- Verdes\n3- Castanhos\n"))
    cor_cabelo= int(input("Insira a cor dos cabelos do entrevistado:\n1- Louros\n2- Castanhos\n3- Pretos\n"))
    
    soma_idd += idade
    
    # a)
    total_entrevistados += 1

    # b)
    if sexo == 1:
        total_h += 1
    else:
        total_m += 1

    # c)
    if idade > maior_idd:
        maior_idd = idade
    


    if sexo == 2 and 18 <= idade <= 35 and cor_olhos == 2 and cor_cabelo == 1:
        indv_ex_total += 1


# d)
media_idd = soma_idd/total_entrevistados

# e)
indv_ex_perc = (indv_ex_total/total_entrevistados)*100

print("Total de entrevistados:", total_entrevistados, 
      "\nTotal de homens:", total_h, 
      "\nTotal de mulheres:", total_m, 
      "\nA maior idade entre os pesquisados é:", maior_idd, 
      "\nE a menor é:", menor_idd, 
      "\nA média de idade é:", media_idd, 
      "\nE a percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros é:", indv_ex_perc)
