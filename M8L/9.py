def CparaF(Celsius):
    return(Celsius * 9/5)+32
def CparaK(Celsius):
    return(Celsius+273)
def KparaC(Kelvin):
    return(Kelvin-273)
def KparaF(Kelvin):
    celsius = KparaC(Kelvin)
    return(CparaF(celsius))
def FparaK (Fahrenheit):
    celsius = (Fahrenheit -32) * 5/9
    return(celsius+273)

def obter_entrada_usuario():
    while True:
        entrada = input("Digite um valor numérico: ")
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def main():
    while True:
        print("-"*60)
        print("Escolha qual conversão você deseja fazer:")
        print("1- Celsius para Fahrenheit")
        print("2- Celsius para Kelvin")
        print("3- Kelvin para Celsius")
        print("4- Kelvin para Fahrenheit")
        print("5- Fahrenheit para Kelvin")
        print("S- Sair do programa")
        opcao = input()

        if opcao == '1':
            print("-"*60)
            celsius = obter_entrada_usuario()
            print(f"{celsius}°C = {CparaF(celsius)}°F")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)

        elif opcao == '2':
            print("-"*60)
            celsius = obter_entrada_usuario()
            print(f"{celsius}°C = {CparaK(celsius)}K")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao == '3':
            print("-"*60)
            kelvin = obter_entrada_usuario()
            print(f"{kelvin}K = {KparaC(kelvin)}°C")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)

        elif opcao == '4':
            print("-"*60)
            kelvin = obter_entrada_usuario()
            print(f"{kelvin}K = {KparaF(kelvin)}°F")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao == '5':
            print("-"*60)
            fahrenheit = obter_entrada_usuario()
            print(f"{fahrenheit}°F = {FparaK(fahrenheit)}K")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue
            print("-"*60)
        
        elif opcao.lower() == "s":
            break
        
        else:
            print("-"*60)
            print("Comando inválido")
            continuar = input("Pressione ENTER para continuar")
            if continuar == "":
                continue

main()
