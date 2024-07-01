# A convenção de graus Fahrenheit para Celsius é obtida pela fórmula 𝑪 = 𝟓. (𝑭 − 𝟑𝟐)/𝟗.
# Escreva um programa que calcule e imprima uma tabela de graus centígrados em
# função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes
# simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5); 

for F in range(50, 150, 5):
    C = int(5*(F-32)/9)
    print(C, "°", " | ", F, "°", end="\n", sep="")