# Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série:
# (100/0!)+(99/1!)+(98/2!)+(97/3!)+...

soma = 100 # Já considera a soma (100/0!)
ponto_de_partida = 99
fatorial = 1

i = 1
while i < 10:
    soma += ponto_de_partida/fatorial
    fatorial = fatorial * (i+1)
    i += 1
    ponto_de_partida -= 1

print(soma)