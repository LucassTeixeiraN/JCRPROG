# Escreva um programa que recebe como entrada um número inteiro n. Em seguida,
# seu programa deve receber as informações de n Pokémon (nome, tipo e ataque). Para
# cada Pokémon seu programa deve armazenar as informações utilizando uma
# estrutura de dicionário. No fim, seu programa deve imprimir o nome do Pokémon do
# tipo “Fogo” com maior ataque. Você pode assumir que os valores de ataque são
# inteiros positivos distintos e que pelo menos um Pokémon do tipo “Fogo” será
# fornecido.

n = int(input("Insira quantos Pokémons serão lidos: "))

pokemon_list = []
maior_atq = 0
pokemon_mais_forte = ""

i = 0
while i < n:
    nome = input("Insira o nome do Pokémon: ")
    tipo = input("Insira o tipo do Pokémon: ")
    atq = int(input("Insira o ataque do Pokémon: "))

    pokemon = {
        "nome": nome,
        "tipo": tipo,
        "atq": atq,
    }

    pokemon_list.append(pokemon)
    i += 1


for i in pokemon_list:
    if i["tipo"].lower() == "fogo" and i["atq"] > maior_atq:
        pokemon_mais_forte = i["nome"]
        maior_atq = i["atq"]

print("O Pokémon com maior ataque é:", pokemon_mais_forte)