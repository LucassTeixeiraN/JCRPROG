#  Uma empresa decidiu dar um bônus de Natal aos seus funcionários, cujo valor é
# definido do seguinte modo:
# a. Funcionários do sexo masculino com tempo de casa superior à 15 anos terão
# direito à um bônus de 15% do seu salário.
# b. Funcionárias com tempo de casa superior à 10 anos terão direito a um bônus
# de 25% do seu salário.
# c. Demais funcionários receberão um bônus de R$ 500,00
# Elabore um programa que leia os dados necessários e calcule o bônus à que tem
# direito o empregado. 

sexo = int(input("Selecione o sexo do funcionário:\n1-Masculino\n2-Feminino\n"))
tempo_de_casa = int(input("Digite o tempo de casa do funcionário em anos "))

if (sexo == 1) & (tempo_de_casa > 15):
    print("O funcionário terá um bônus de 15% do seu salário")
elif (sexo == 2) & (tempo_de_casa > 10):
    print("A funcionário terá um bônus de 25% do seu salário")
else:
    print("O funcionário terá um bônus de R$ 500")