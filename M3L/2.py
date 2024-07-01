# Em um determinado país, deve declarar imposto de renda todo cidadão com renda
# anual superior à $ 23.750,00. A renda anual é a renda mensal multiplicada por 13 (12
# meses mais a o 13º salário). A alíquota para quem paga é de 20%. Faça um programa
# que leia do teclado a renda mensal do usuário e imprima se ele está isento ou se ele
# deve fazer a declaração de renda e qual o imposto devido. Declare como constantes
# simbólicas o limite para imposto: 23750; o fator de multiplicação: 13; e a alíquota:
# 20%. 

salario = float(input("Insira o seu salário: "))
limite_isencao = 23750
fator_multiplicacao = 13
aliquota = 0.2

salario_anual = salario * fator_multiplicacao
imposto = salario_anual*aliquota

if salario_anual > limite_isencao:
    print('Você deve pagar $', imposto, 'de imposto')
else:
    print('Você está isento de impostos')
