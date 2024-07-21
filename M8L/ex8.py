'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo: C =5/9*(F-32).
A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

def FparaC(F):
    C = 5/9*(F-32)
    return C

def main():
    while True:
        try:
            print(70*"-")
            F = input("Digite os graus em °F (Deixe em branco para sair do programa): ")
            if F == "":
                print("\nEncerrado!")
                break
            F = int(F)
            print(f"\nConversao para graus °C: {FparaC(F):.2f}")
        except ValueError:       
            print("\nDados invalidos")
            print(70*"-")
                
main()
