# Um dado material radioativo perde metade de sua massa a cada 50 s. Dada a massa
# inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
# essa massa seja menor que 0,5g.

massa = float(input("Insira a massa do material radioativo: "))
tempo = 0

while massa >= 0.5:
    tempo += 50
    massa = massa / 2

print(tempo, "segundos")