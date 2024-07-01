# O número pi pode ser calculado através da série:
# pi = 4 - (4/3) + (4/5) - (4/7) + (4/9) - ... Faça um
# programa para calcular o valor de pi com precisão de 0,00001 (o programa encerra
# quando a parcela da série for menor que a precisão)

precisão = 0.00001
serie = 0 # Valor da série que vai se aprocimar do valor de pi
divisor = 1 # Número que vai dividir o 4 
soma = True # Variável que vai ser usada para saber se a parcela deve ser somada ou subtraída do resto da série
parcela = 4

while parcela >= precisão:
    parcela = 4/divisor # A cada loop redefine o valor da parcela

    if soma == True: # Significa que vai ser realizado uma soma
        serie += parcela
        soma = False
    else: # Significa que vai ser realizado uma subtração
        serie -= parcela
        soma = True

    divisor += 2 # A cada loop é somado 2 ao divisor
    print(parcela)
print(serie)