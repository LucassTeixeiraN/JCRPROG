'''
Faça um programa que conta quantos caracteres únicos existem em uma string. A
string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas
um. Utilize um dicionário para resolver esse problema.
'''
string = input("Insira um texto para saber quantos caracteres únicos ele possui: \n")
caracteres = {}

for i in range(len(string)):
    if string[i] not in caracteres:
        caracteres[string[i]] = 1
    else:
        caracteres[string[i]] += 1

print(f'O texto possui {len(caracteres)} únicos.')