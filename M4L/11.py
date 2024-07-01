# O volume de uma esfera pode ser calculado pela fórmula
# V = (4/3)*pi*r^3, onde r é o raio da
# esfera. Faça um programa que imprima uma tabela de volumes para esferas que
# tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.

pi = float(input("Insira o valor de pi: "))

for r in list(range(0, 155, 5)): # raio em milimetros
    r = r/10 # conversão para centimetros
    volume = (4/3)*pi*r**3
    print(volume)
