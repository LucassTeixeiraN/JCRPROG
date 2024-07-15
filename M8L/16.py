'''Faça um programa que calcule o imposto de renda de um contribuinte de um país imaginário
onde as regras do imposto são as seguintes:
• Todos pagam a mesma alíquota, de 20%.
• São descontados da base de cálculo (proventos) as despesas com educação e despesas
médicas.
• São descontados R$ 1000,00 por dependente.
• O imposto devido ou a receber pode ser parcelado em até 6 vezes.
• Valores de imposto (devido ou a receber) abaixo de R$100,00 não são cobrados nem
pagos.'''


def calcImposto(salario, despesas, n_dependentes):

    imposto_bruto = (salario * 12)*0.2

    imposto_liquido = imposto_bruto - despesas - n_dependentes*1000

    return imposto_liquido

def main():
    salario = input("Insira seu salário: ")
    despesas = input("Insira a soma de suas despesas médicas e relacionadas a educação: ")
    n_dependentes = input("Insira quantos dependentes você possui: ")

    if not salario.isalpha() and float(salario) >= 0 and not despesas.isalpha() and float(despesas) >= 0 and n_dependentes.isnumeric() and int(n_dependentes) >= 0:
        imposto = calcImposto(float(salario), float(despesas), int(n_dependentes))

        if not -100 < imposto < 100:
            if imposto > 0:
                print(f"Você deve pagar R${round(imposto, 2)}, podendo parcelar em até 6x de R${round(imposto/6, 2)}")
            else:
                print(f"Você deve receber R${round(imposto*(-1), 2)}, podendo receber em até 6x de R${round((imposto*-1)/6, 2)}")
        else:
            print("Você não tem valores a receber ou pagar")
    else:
        print("Valores inválidos")

main()