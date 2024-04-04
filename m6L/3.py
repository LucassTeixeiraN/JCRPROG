# Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da
# esquerda para a direita como da direita para a esquerda (desconsiderando os
# espaços em branco). Considere que a entrada não possui sinais de pontuação ou
# acentos. Escreva um programa que, dada uma String, verifique se ela é um
# palíndromo

texto = input("Insira uma frase ou palavra para saber se ela é ou não um palíndromo: ")

if texto.replace(" ","").lower() == texto.replace(" ","").lower()[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")