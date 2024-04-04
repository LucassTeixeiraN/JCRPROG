# Para enviar mensagens que não devem ser lidas por estranhos, pode-se codificá-las.
# Faça um programa que leia uma frase e a seguir codifique essa frase da seguinte
# forma: cada letra que se encontra em posição ímpar na tabela ASCII tem este seu
# valor ASCII dividido por 2, e cada letra que se encontra em posição par na mesma
# tabela é trocada por outra, 3 posições atrás dela da tabela. No final, imprima a frase
# codificada.

texto = input("Insira a frase a ser codificada: ")
texto_cod = ""

for i in range(len(texto)):
    caracter = ord(texto[i])

    if caracter % 2 == 0:
        texto_cod += chr(caracter + 3)

    else:
        texto_cod += chr(caracter // 2)

print("-"*15)
print("Frase codificada:", texto_cod)
print("-"*15)