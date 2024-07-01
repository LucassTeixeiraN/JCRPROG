'''
A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário
com os campos saldo, com o saldo devedor da conta, transações, com o número de
transações que gerou esse saldo, e média, com a média de gastos por transação. O
programa deve preencher o dicionário com a conta e o valor da compra e gerar um
novo dicionário para aquela conta, com o saldo devedor, número de transações e
média de gastos atualizados.
'''

conta = {
    "saldo": 0,
    "transacao": 0,
    "media": 0,
}

while True:
    gasto = input("Insira um novo gasto (se não há mais gastos digite 0): ")
    if gasto == "0":
        break 

    if not gasto.isalpha():
        gasto = float(gasto)
        conta["saldo"] += gasto
        conta["transacao"] += 1
    else:
        print("insira um valor numérico para o gasto")

conta["media"] = conta["saldo"]/conta["transacao"]

print("-"*30)
print("A nova conta terá:")
print("Saldo: R${saldo:.2f}".format(saldo = conta["saldo"]))
print(f"Número de transações: {conta['transacao']}")
print(f"Média de gasto por transação: {conta['media']}")
print("-"*30)
