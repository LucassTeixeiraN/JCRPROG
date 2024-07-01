'''
Escreva um programa que conta todas as vogais presentes no texto recebido como
parâmetro e retorna um dicionário contendo a quantidade de cada vogal. Seu
programa deve exibir, no fim, os dados do dicionário retornado.
'''

texto = input("Insira um texto para saber quantas vogais de cada ele possui: \n")
# VOGAIS = ('a', 'e', 'i', 'o', 'u')
vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}

for i in range(len(texto)):
    if texto[i] in vogais:
        vogais[texto[i]] += 1

print('-'*30)
print(f'a: {vogais["a"]}')
print(f'e: {vogais["e"]}')
print(f'i: {vogais["i"]}')
print(f'o: {vogais["o"]}')
print(f'u: {vogais["u"]}')
print('-'*30)