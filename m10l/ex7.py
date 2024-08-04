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
    while True:
        caractere = input("\nQue caractere deseja procurar?(digite 'stop' quando quiser sair do programa): ")
        if caractere.lower() == 'stop':
            print("Saindo do programa.")
            break
        else:
            if len(caractere) == 1: 
                contar = ocorrencias(string, caractere)
                print(f"\nO caractere '{caractere}' aparece {contar} vezes na string")
            else:
                print("\nERRO: Procure por apenas um caractere por vez!")
main()
