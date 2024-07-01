# Escreva um programa que, dada uma String representando um texto, imprima o
# número de palavras existentes. Observação: você deve remover os sinais de
# pontuação (“.”, “,”, “:”, “;”, “!” e “?”) antes de realizar a contagem das palavras.

PONTUACAO = ('.', ',', ':', ';', '!', '?')
frase = input("Insira uma frase para saber quantas palavras ela possui: ")
frase_sem_pontuacao = ""

for i in range(len(frase)):
    if not frase[i] in PONTUACAO:
        frase_sem_pontuacao += frase[i]

frase_sem_pontuacao = frase_sem_pontuacao.split(" ")
c = frase_sem_pontuacao.count("")

for i in range(c):
    frase_sem_pontuacao.remove("")

print("-"*60)
print(f"A frase: {" ".join(frase_sem_pontuacao)}")
print(f"Possui: {len(frase_sem_pontuacao)} palavras")
print("-"*60)