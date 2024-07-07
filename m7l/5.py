'''
A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário
com os campos saldo, com o saldo devedor da conta, transações, com o número de
transações que gerou esse saldo, e média, com a média de gastos por transação. O
programa deve preencher o dicionário com a conta e o valor da compra e gerar um
novo dicionário para aquela conta, com o saldo devedor, número de transações e
média de gastos atualizados.
'''
saldo = input("Insira o saldo da conta: ")
transacao = input("Insira o número de transações da conta: ")

# Verifica se os valores do input são válidos 
if not saldo.isalpha() and float(saldo) >= 0 and transacao.isnumeric() and int(transacao) >= 0:
    saldo = float(saldo)
    transacao = int(transacao)
    if transacao != 0:
        media = saldo/transacao
    else:
        saldo = 0
        media = 0

    conta = {
        "saldo": saldo,
        "transacao": transacao,
        "media": media,
    }

    while True:
        gasto = input("Insira um novo gasto (se não há mais gastos aperte ENTER): ")
        if gasto == "":
            break 
        
        if not gasto.isalpha():
            gasto = float(gasto)
            conta["saldo"] += gasto
            conta["transacao"] += 1
        else:
            print("insira um valor numérico para o gasto")

    if conta["transacao"] != 0:
        conta["media"] = conta["saldo"]/conta["transacao"]
    else:
        conta["media"] = 0

    print("-"*30)
    print("A nova conta terá:")
    print(f"Saldo devedor: R${conta["saldo"]:.2f}")
    print(f"Número de transações: {conta['transacao']}")
    print(f"Média de gasto por transação: R${conta["media"]:.2f}")
    print("-"*30)

else:
    print("Insira valores válidos nos campos de saldo e transação")