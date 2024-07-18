'''A multiplicação entre dois números inteiros pode ser definida como uma repetição da
adição de um deles. Exemplo: 3x4 = 4 + 4 + 4. Escreva uma função que multiplique
dois números inteiros utilizando esse método. A seguir, escreva um programa que
peça ao usuário um número inteiro e imprima a tabuada para aquele número (de 1 à
10) utilizando a função construída.'''

def multiplicacao(a,b):
    resp = f"{a}x{b} = "

    for i in range(b):
        if a > 0:
            if i < b-1:
                resp += f"{a} + "
            else:
                resp += f"{a} = {a*b}"
        else:
            if i < b-1:
                resp += f"({a}) + "
            else:
                resp += f"({a}) = {a*b}"

    return resp

def main():
    numero = input("Insira um número para ver sua tabuada: ")

    while True:
        try:
            numero = int(numero)
            break
        except ValueError:
            print("Insira um número inteiro.")

    print('-'*50)
    for i in range(1,11):
        print(multiplicacao(numero,i))
    print('-'*50)

main()
