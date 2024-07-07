# Faça um programa que leia uma frase e inverta todas as letras maiúsculas para
# minúsculas e vice-versa. Além disso, o programa deve colocar um hífen no lugar de
# todos os espaços em branco.

frase = input("Insira uma frase para que seus espaços sejam substituídos por hífen, suas letras maiúsculas por minúsculas e vice-versa: ")
nova_frase = ""

for i in range(len(frase)):
    if frase[i] == " ":
        nova_frase += "-"
    elif frase[i].isalpha() and frase[i].lower() == frase[i]:
        nova_frase += frase[i].upper()
    elif frase[i].isalpha() and frase[i].upper() == frase[i]:
        nova_frase += frase[i].lower()
    else:
        nova_frase += frase[i]

print("-"*65)
print(f"Frase original: {frase}")
print(f"Nova frase: {nova_frase}")
print("-"*65)