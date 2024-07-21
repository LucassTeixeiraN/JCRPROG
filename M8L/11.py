'''O seno de um ângulo em radianos, no intervalo de 0 à π/2 pode ser calculado através
da série de McLaurin, apresentada a seguir:
sen x = x/1! + x³/3! + x^5/5! + ...
a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180° = π rad)
b. Escreva uma função que receba como parâmetro um ângulo em graus, a precisão
requerida para o cálculo e retorne o seu seno, utilizando a função de conversão
graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno. '''

PI = 3,14

def grauParaRad(x):
    rad = x/180
    return rad


def calcSeno(graus, prec):

    rad = grauParaRad(graus)
    
    seno = f'sen {rad}π rad = '


    resultado = 0
    #Número que eleva o x
    n = 1
    for i in range(prec):
        fatorial = 1
        for j in range(1, n+1):
            fatorial *= j

        resultado += ((rad*PI)**n)/fatorial

        if i < prec-1:
            seno += f'{rad}π^{n}/{n}! + '
        else:
            seno += f'{rad}π^{n}/{n}! = {resultado}'

        n += 2
    print(seno)


def main():

    while True:
        try:
            grau = float(input("Insira um ângulo em grau e descubra seu seno: "))
            prec = int(input("Insira a precisão do cálculo (o número inserido será a quantidade de operações feitas no cálculo do seno): "))
            break
        except ValueError:
            print("Valores inválidos")


    if 0 <= grau <= 90 and prec > 0:
        calcSeno(grau, prec)
    else:
        print("Valores inválidos. Tente inserir entre 0° e 90°, além de uma precisão inteira e positiva")

main()
