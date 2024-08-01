'''
Escreva uma função recursiva que, dada uma string s e um caractere c, conte o
número de ocorrências do caractere c na string s.
'''
def ocorrencias(s, c):
    if not s:
        return 0
    elif s[0] == c:
        return 1 + ocorrencias(s[1:], c)
    else:
        return ocorrencias(s[1:], c)
    
def main():
    string = input("Digite uma frase: ")
    caractere = input("Que caractere deseja procurar: ")
    contar = ocorrencias(string, caractere)
    print(f"A letra '{caractere}' aparece {contar} vezes na string")
main()