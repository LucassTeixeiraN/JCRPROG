'''Escreva uma função que, dados dois números inteiros positivos, calcule e retorne o
Máximo Divisor Comum (MDC) entre os dois.

Escreva também uma função que, dada uma lista de três ou mais números inteiros positivos, 
calcule e retorne o Máximo
Divisor Comum (MDC) entre eles. A seguir, escreva um programa para testar essas
funções.'''

def mdc(a, b):

    while b:
        a, b = b, a % b
    return a

def mdc_lista(numeros):
    
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mdc(resultado, num)
    return resultado

def main():
    # Teste com dois numeros
    a = input("Digite o primeiro numero: ")
    b = input("Digite o segundo numero: ")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        
        print(f"MDC({a}, {b}) = {mdc(a, b)}")
    else:
        print("Insira um numeros validos")

    # Teste com lista de numeros
    numeros = [12, 18, 24, 30]
    print(f"MDC da lista {numeros} = {mdc_lista(numeros)}")
if __name__ == "__main__":
    main()
