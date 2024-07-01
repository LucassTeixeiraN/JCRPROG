# Construa um programa que receba três valores quaisquer e imprima-os em ordem
# crescente. Como seu programa reage a valores de entrada iguais como no exercício
# anterior?

a=int(input("Escreva um número inteiro: "))
b=int(input("Escreva uma número inteiro: "))
c=int(input("Escreva uma número inteiro: "))

if a < b and a < c and b < c: 
    print( a , b , c , sep="<")
elif a < b and a < c and  c < b:
    print ( a , c , b, sep="<")
elif b < a and b < c and a < c:
    print(  b , a ,  c, sep="<")
elif b < a and b < c and c < a:
    print( b , c , a, sep="<")
elif c < a and c < b and a < b:
    print( c , a , b, sep="<")
elif c < a and c < b and b < a:
    print(c , b , a, sep="<")
else:
    print("Insira números diferentes")


print("End of program")