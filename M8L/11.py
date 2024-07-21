'''O seno de um ângulo em radianos, no intervalo de 0 à π/2 pode ser calculado através
da série de McLaurin, apresentada a seguir:
sen x = x/1! + x³/3! + x^5/5! + ...
a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180° = π rad)
b. Escreva uma função que receba como parâmetro um ângulo em graus, a precisão
requerida para o cálculo e retorne o seu seno, utilizando a função de conversão
graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno. '''

PI = 3,14  # Definição do valor de PI

# Função para converter um ângulo de graus para radianos
def grauParaRad(x):
    rad = x / 180  # Converte graus para radianos
    return rad

# Função para calcular o seno utilizando a série de McLaurin
def calcSeno(graus, prec):
    rad = grauParaRad(graus)  # Converte o ângulo de graus para radianos
    
    seno = f'sen {rad}π rad = '  # Inicia a string de resposta com a conversão

    resultado = 0
    n = 1  # Número que eleva o x
    for i in range(prec):
        fatorial = 1
        for j in range(1, n + 1):
            fatorial *= j  # Calcula o fatorial de n

        resultado += ((rad * PI) ** n) / fatorial  # Adiciona o termo da série ao resultado

        if i < prec - 1:
            seno += f'{rad}π^{n}/{n}! + '  # Adiciona o termo da série à string de resposta
        else:
            seno += f'{rad}π^{n}/{n}! = {resultado}'  # Adiciona o termo final e o resultado à string de resposta

        n += 2  # Incrementa n para o próximo termo da série
    print(seno)  # Imprime a string de resposta

# Função principal para obter a entrada do usuário e calcular o seno
def main():
    while True:
        try:
            grau = float(input("Insira um ângulo em grau e descubra seu seno: "))  # Solicita o ângulo em graus
            prec = int(input("Insira a precisão do cálculo (o número inserido será a quantidade de operações feitas no cálculo do seno): "))  # Solicita a precisão do cálculo
            break
        except ValueError:
            print("Valores inválidos")  # Mensagem de erro para entradas inválidas

    if 0 <= grau <= 90 and prec > 0:
        calcSeno(grau, prec)  # Calcula o seno se os valores forem válidos
    else:
        print("Valores inválidos. Tente inserir entre 0° e 90°, além de uma precisão inteira e positiva")  # Mensagem de erro para valores fora do intervalo

# Chama a função principal se o script for executado diretamente
main()

