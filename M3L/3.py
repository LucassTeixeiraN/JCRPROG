# Escreva um programa que, dadas duas datas, determine qual delas ocorreu
# cronologicamente primeiro. Para cada uma das duas datas, leia três números
# referentes ao dia, mês e ano, respectivamente

dia1 = int(input("Insira o dia da primeira data: "))
mes1 = int(input("Insira o mês da primeira data: "))
ano1 = int(input("Insira o ano da primeira data: "))

dia2 = int(input("Insira o dia da segunda data: "))
mes2 = int(input("Insira o mês da segunda data: "))
ano2 = int(input("Insira o ano da segunda data: "))

if ano1 < ano2:
    print("A primeira data ocorreu primeiro")
elif ano1 > ano2:
    print("A segunda data ocorreu primeiro")
else:
    if mes1 < mes2:
        print("A primeira data ocorreu primeiro")
    elif mes1 > mes2:
        print("A segunda data ocorreu primeiro")
    else:
        if dia1 < dia2:
            print("A primeira data ocorreu primeiro")
        elif dia1 > dia2:
            print("A segunda data ocorreu primeiro")
        else:
            print("As duas datas são iguais")
