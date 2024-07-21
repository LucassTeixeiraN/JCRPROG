'''Faça um programa que calcule o imposto de renda de um contribuinte de um país imaginário
onde as regras do imposto são as seguintes:
• Todos pagam a mesma alíquota, de 20%.
• São descontados da base de cálculo (proventos) as despesas com educação e despesas
médicas.
• São descontados R$ 1000,00 por dependente.
• O imposto devido ou a receber pode ser parcelado em até 6 vezes.
• Valores de imposto (devido ou a receber) abaixo de R$100,00 não são cobrados nem
pagos.'''

ALIQUOTA = 0.2
DESCONTO_POR_DEPENDENTE = 1000

def calcImposto(salario, despesas, n_dependentes):

    imposto_bruto = (salario * 12)*ALIQUOTA

    imposto_liquido = imposto_bruto - despesas - n_dependentes*DESCONTO_POR_DEPENDENTE

    return imposto_liquido

def verifSituacaoPagamento(imposto):
    if not -100 < imposto < 100:
        if imposto > 0:
            print(f"Você deve pagar R${imposto:.2f}, podendo parcelar em até 6x de R${(imposto/6):.2f}")
            print('-'*60)
        else:
            print(f"Você deve receber R${imposto*(-1):.2f}, podendo receber em até 6x de R${((imposto*-1)/6):.2f}")
            print('-'*60)
    else:
        print("Você não tem valores a receber ou pagar")
        print('-'*60)

def main():

    while True:
        try:
            print('-'*60)
            salario = float(input("Insira seu salário: "))
            despesas = float(input("Insira a soma de suas despesas médicas e relacionadas a educação: "))
            n_dependentes = int(input("Insira quantos dependentes você possui: "))
            print('\n')
            break
        except ValueError:
            print("Valor inválido")

    imposto = calcImposto(salario, despesas, n_dependentes)

    verifSituacaoPagamento(imposto)

main()
