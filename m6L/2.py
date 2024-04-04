# Escreva um programa que, dada uma String representando um texto, imprima o
# número de palavras existentes. Observação: você deve remover os sinais de
# pontuação (“.”, “,”, “:”, “;”, “!” e “?”) antes de realizar a contagem das palavras.

texto = input("Insira um texto para que o progama conte seu número de palavras: ")
PONTUACOES = (".", ",", ":", ";", "!", "?")
lista = []
contador = 0

for i in range(len(texto)):
    if not(texto[i] in PONTUACOES):
        lista.append(texto[i])

novo_texto = "".join(lista)

for i in novo_texto.split():
    contador += 1

print("-"*15)
print("Frase:", texto)
print("Frase sem pontuações:", novo_texto)
print("Número de palavras:", contador)
print("-"*15)