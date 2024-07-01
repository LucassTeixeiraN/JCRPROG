# Desejamos calcular, a partir do sexo e da altura, o peso ideal de uma pessoa. Para
# isto, devemos saber que existem duas fórmulas para o peso ideal, que são:
# • Homens: (72,7 * altura) - 58
# • Mulheres: (62,1 * altura) - 44,7
# Para que uma pessoa seja considerada obesa, a diferença entre o seu peso e o peso
# ideal deve ser superior à 40 Kg. Elabore um programa que leia o sexo, o peso e a
# altura de uma pessoa, imprima o peso ideal e informe se a pessoa está abaixo do
# peso ideal, acima do peso ideal ou obesa. 

altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))
sexo = input("Insira seu sexo (masculino ou feminino): ")

peso_ideal_h = 72.7 * altura - 58
peso_ideal_m = 62.1 * altura - 44.7

if sexo == "masculino":
    if peso - peso_ideal_h > 40:
        print("Seu peso ideal é", peso_ideal_h, "\nvocê está obeso")
    elif peso - peso_ideal_h <= 40 and peso - peso_ideal_h > 0:
        print("Seu peso ideal é", peso_ideal_h, "\nvocê está acima do peso ideal")
    elif peso - peso_ideal_h < 0:
        print("Seu peso ideal é", peso_ideal_h, "\nvocê está abaixo do peso ideal")
    else:
        print("Você está no peso ideal")
else:
    if peso - peso_ideal_m > 40:
        print("Seu peso ideal é", peso_ideal_m, "\nvocê está obesa")
    elif peso - peso_ideal_m <= 40 and peso - peso_ideal_m > 0:
        print("Seu peso ideal é", peso_ideal_m, "\nvocê está acima do peso ideal")
    elif peso - peso_ideal_m < 0:
        print("Seu peso ideal é", peso_ideal_m, "\nvocê está abaixo do peso ideal")
    else:
        print("Você está no peso ideal")
