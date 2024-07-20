'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo: C =5/9*(F-32)
 . A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

def FparaC(F):
    C = 5/9*(F-32)
    return C
def main():
    while True:
        try:
            F = int(input("Digite os graus em F:"))
            print(50*"-")
        except ValueError:       
            print("Dados invalidos")
                
                    
        print(f"Conversao para graus C:{FparaC(F):.2f}")
        print(50*"-")
           
        print("Encerrado")
        break
main()
