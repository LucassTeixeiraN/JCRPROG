# Elabore um programa que dado o peso de um boxeador, informe à categoria a qual
# pertence, seguindo a tabela abaixo.

peso = float(input("Insira o peso do boxeador: "))

if peso < 50:
    print("O boxeador pertence a categoria palha")
elif peso < 59:
    print("O boxeador pertence a categoria pluma")
elif peso < 75:
    print("O boxeador pertence a categoria leve")
elif peso < 87:
    print("O boxeador pertence a categoria pesado")
else:
    print("O boxeador pertence a categoria super pesado")