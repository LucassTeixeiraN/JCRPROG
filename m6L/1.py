# Faça um programa que leia uma frase, e duas letras quaisquer do usuário. A seguir,
# troque na frase todas as ocorrências da primeira letra fornecida pela segunda e
# imprima a nova frase.

frase = input("Insira uma frase: ")
l1 = input("Insira a letra que deverá ser trocada: ")
l2 = input("Insira que entrará no lugar da letra trocada: ")
nova_frase = ""

if len(frase) == 0:
    print("Você deve inserir uma frase") 
elif len(l1) == 0 or len(l1) > 1 or len(l2) == 0 or len(l2) > 1 :
    print("Você deve inserir apenas uma letra nos campos de qual letra deve ser trocada e no de qual será a letra que irá substituir a anterior")
else:
    for i in range(len(frase)):
        if frase[i] == l1.lower():
            nova_frase += frase[i].replace(l1, l2)
        elif frase[i] == l1.capitalize():
            nova_frase += frase[i].replace(l1.capitalize(), l2.capitalize())
        else:
            nova_frase += frase[i] 

print(nova_frase)
