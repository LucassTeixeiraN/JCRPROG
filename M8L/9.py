""". Escreva as seguintes funções:
a. CparaF – faz a conversão de uma temperatura em graus C para graus F.
b. CparaK – faz a conversão de uma temperatura em C para Kelvin (C=K-273)
c. KparaC – faz a conversão de K para C.
d. KparaF – faz a conversão de K para F (dica: utilize as funções anteriores)
e. FparaK – faz a conversão de F para K. """

def CparaF(Celsius):
    return(Celsius * 9/5)+32
def CparaK(Celsius):
    return(Celsius+273)
def KparaC(Kelvin):
    return(Kelvin-273)
def KparaF(Kelvin):
    Celsius = KparaC(Kelvin)
    return(Kelvin)
def FparaK (Fahrenheit):
    celsius = (Fahrenheit -32) * 5/9
    return(Fahrenheit)

def obter_entrada_usuario():
    while True:
        entrada = input("Digite um valor numérico: ")
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


print("Conversão de Celsius para Fahrenheit:")
celsius = obter_entrada_usuario()
print(f"{celsius}°C = {CparaF(celsius)}°F")

print("\nConversão de Celsius para Kelvin:")
celsius = obter_entrada_usuario()
print(f"{celsius}°C = {CparaK(celsius)}K")

print("\nConversão de Kelvin para Celsius:")
kelvin = obter_entrada_usuario()
print(f"{kelvin}K = {KparaC(kelvin)}°C")

print("\nConversão de Kelvin para Fahrenheit:")
kelvin = obter_entrada_usuario()
print(f"{kelvin}K = {KparaF(kelvin)}°F")

print("\nConversão de Fahrenheit para Kelvin:")
fahrenheit = obter_entrada_usuario()
print(f"{fahrenheit}°F = {FparaK(fahrenheit)}K")

