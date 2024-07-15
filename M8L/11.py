'''O seno de um ângulo em radianos, no intervalo de 0 à π/2 pode ser calculado através
da série de McLaurin, apresentada a seguir:
sen x = x/1! + x³/3! + x^5/5! + ...
a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180° = π rad)
b. Escreva uma função que receba como parâmetro um ângulo em graus, a precisão
requerida para o cálculo e retorne o seu seno, utilizando a função de conversão
graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno. '''


def grauParaRad(x):

    rad = x/180
    return rad


def calcSeno(graus, prec):

    rad = grauParaRad(graus)
    
    seno = f'sen {rad}π rad = '


    # Tentar deixar mais claro esse loop
    resultado = 0
    n = 1
    for i in range(prec):
        fatorial = 1
        for j in range(1, n+1):
            fatorial *= j

        resultado += (rad**n)/fatorial

        if i < prec-1:
            seno += f'{rad}^{n}/{n}! + '
        else:
            seno += f'{rad}^{n}/{n}! = {resultado}'

        n += 2
    print(seno)


def main():
    grau = input("Insira um ângulo em grau e descubra seu seno: ")
    prec = input("Insira a precisão do calculo (o número inserido será a quantidade de operações feitas no cálculo do seno): ")

    if not grau.isalpha() and prec.isnumeric() and int(prec) > 0:
        calcSeno(float(grau), int(prec))

main()
