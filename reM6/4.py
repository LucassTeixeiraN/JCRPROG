# Para enviar mensagens que não devem ser lidas por estranhos, pode-se codificá-las.
# Faça um programa que leia uma frase e a seguir codifique essa frase da seguinte
# forma: cada letra que se encontra em posição ímpar na tabela ASCII tem este seu
# valor ASCII dividido por 2, e cada letra que se encontra em posição par na mesma
# tabela é trocada por outra, 3 posições atrás dela da tabela. No final, imprima a frase
# codificada.

mensagem = input("Insira a mensagem que será codificada: ")
msg_codificada = ""

for i in range(len(mensagem)):
    if ord(mensagem[i])%2 == 0:
        msg_codificada += chr(ord(mensagem[i]) - 3)
    else:
        msg_codificada += chr(ord(mensagem[i])//2)

print(f"Frase codificada:{msg_codificada}")
