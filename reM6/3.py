# Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da
# esquerda para a direita como da direita para a esquerda (desconsiderando os
# espaços em branco). Considere que a entrada não possui sinais de pontuação ou
# acentos. Escreva um programa que, dada uma String, verifique se ela é um
# palíndromo.

frase = input("Insira uma frase para verificar se ela é um palíndromo: ")
frase_sem_espaco = frase.replace(" ","")

print("-"*65)
if frase_sem_espaco.lower() == frase_sem_espaco[::-1].lower():
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

print(f"\nFrase original: {frase}")
print(f"\nFrase invertida: {frase[::-1]}")
print("-"*65)

# Ex:
# ze de lima rua laura mil e dez
# socorram me subi no onibus em marrocos 