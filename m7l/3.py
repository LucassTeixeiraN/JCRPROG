'''
Faça um programa que conta quantos caracteres únicos existem em uma string. A
string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas
um. Utilize um dicionário para resolver esse problema.
'''
string = input("Insira um texto para saber quantos caracteres únicos ele possui: \n")
caracteres = {}

for i in range(len(string)):
    # Verifica se o caracter já foi lido, caso não, ele é adicionado no dicionário caracteres
    if string[i] not in caracteres:
        caracteres[string[i]] = 1
        
# É printado o número de chaves do dicionário, que é o número de caracteres unicos
print(f'O texto possui {len(caracteres)} caracteres únicos.')
