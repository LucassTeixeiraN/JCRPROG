'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo: C =5/9*(F-32)
 . A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

def FparaC(F):
    C = 5/9*(F-32)
    return C

while True:
   
    F = input("Digite Graus F:")
    print(50*"-")
    if not F.isalpha():
        F = float(F)
        print(f"Conversao para graus C:{FparaC(F)}")
        print(50*"-")
    elif F == "no":
        print("Encerrado")
        break
        
    else:
        print("Dados invalidos")
