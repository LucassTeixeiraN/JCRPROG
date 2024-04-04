# Faça um programa que leia uma frase e inverta todas as letras maiúsculas para
# minúsculas e vice-versa. Além disso, o programa deve colocar um hífen no lugar de
# todos os espaços em branco.
texto = input("Insira uma frase: ")
novo_texto = ""

for i in range(len(texto)):
    if texto[i] == " ":
        novo_texto += "-"
    elif texto[i] == texto[i].capitalize():
        novo_texto += texto[i].lower()
    elif texto[i] == texto[i].lower():
        novo_texto += texto[i].capitalize()
    else:
        novo_texto += texto[i]

print(novo_texto)