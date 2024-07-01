# Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são
# fornecidos os seguintes dados:
# • O preço o kWh
# • O número de identificação de cada consumidor
# • A quantidade de kWh consumido no mês por cada um
# • O código do tipo de consumidor (residencial, comercial ou industrial)
# A partir desses dados calcule:
# a. Para cada consumidor, o total à pagar;
# b. O maior consumo verificado;
# c. O menor consumo verificado
# d. O total de consumo (em kWh) para cada um dos três tipos de consumidores
# e. A média de consumo (em kWh) para cada um dos três tipos de consumidores
# f. O total arrecadado pela companhia elétrica. 

preco_kwh = float(input("Insira o preço do kWh: "))

consumo_total_res = consumo_total_com = consumo_total_ind = 0
maior_consumo = menor_consumo = 0
res = com = ind = 0 # número de consumidores de cada tipo
total_arrecadado = 0


while True:
    n_indentificador = int(input("Insira o número de identificador do consumidor: "))
    qntd_kwh = int(input("Insira a quantidade de kWh consumida por mês pelo consumidor: "))
    codigo = int(input("Em qual tipo dos três tipos a seguir o consumidor se encaixa:\n1-Residencial\n2-Comercial\n3-Industrial\n"))


    pagamento_individual = qntd_kwh * preco_kwh

    print("O consumidor", n_indentificador, "deverá pagar", pagamento_individual)

    total_arrecadado += pagamento_individual
    
    
    # Conta o número de consumidores e soma o consumo de cada tipo 
    if codigo == 1: #residencial
        consumo_total_res += qntd_kwh
        res += 1 
    elif codigo == 2: #comercial
        consumo_total_com += qntd_kwh
        com += 1
    else: #industrial
        consumo_total_ind += qntd_kwh
        ind += 1


    if qntd_kwh > maior_consumo:
        maior_consumo = qntd_kwh
        maior_consumo_id = n_indentificador

    if menor_consumo == 0 or qntd_kwh < menor_consumo:
        menor_consumo = qntd_kwh
        menor_consumo_id = n_indentificador


    fim = int(input("Deseja adicionar mais algum consumidor?\n1-Sim\n2-Não\n"))
    
    if fim == 2:
        break

# Calculo das médias
# e)
if res != 0:
    media_consumo_res = consumo_total_res/res
else:
    media_consumo_res = 0

if com != 0:
    media_consumo_com = consumo_total_com/com
else:
    media_consumo_com = 0

if ind != 0:
    media_consumo_ind = consumo_total_ind/ind
else:
    media_consumo_ind = 0


print("O maior consumo foi do número de dentificação ", maior_consumo_id, 
      "\nO menor consumo foi do número de dentificação ", menor_consumo_id, 
      "\nO total consumido por cada tipo foi:\nResidencial: ", consumo_total_res, 
      "\nComercial: ", consumo_total_com, 
      "\nIndustrial: ", consumo_total_ind, 
      "\nA média de consumo para cada um dos tipos de consumidores foi:\nResidencial: ", media_consumo_res, 
      "\nComercial: ", media_consumo_com, 
      "\nIndustrial: ", media_consumo_ind, 
      "\nE a companhia arrecadou um total de R$ ", total_arrecadado, sep="")

