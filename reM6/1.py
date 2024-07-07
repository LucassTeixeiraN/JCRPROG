# Faça um programa que leia uma frase, e duas letras quaisquer do usuário. A seguir,
# troque na frase todas as ocorrências da primeira letra fornecida pela segunda e
# imprima a nova frase.

frase = input("Insira uma frase: ")
frase_nova = ''
letra_antiga = input("Insira a letra que será trocada: ")
letra_nova = input("Insira a letra que será inserida no lugar da anterior: ")

if len(frase) > 0 and len(letra_antiga) == 1 and len(letra_nova) == 1:

    for i in range(len(frase)):
        if frase[i] == letra_antiga:
            frase_nova += letra_nova
        else:
            frase_nova += frase[i]
    
    print("-"*60)
    print(f"Frase antiga: {frase}")
    print(f"Frase nova: {frase_nova}")
    print("-"*60)

else:
    print("-"*60)
    print("Os valores inseridos são inválidos. Tente novamente.")
    print("-"*60)