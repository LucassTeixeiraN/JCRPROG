# Utilizando-se do comando if else aninhado, elabore um programa que:
# • Mostre um menu de opções de conversão entre moedas (1 – dólar americano,
# 2 – euro, 3 – libra esterlina e 4 – yuan;
# • Leia a escolha do usuário;
# • Leia o custo em R$ (reais) da operação;
# • Imprima o valor da transação na moeda escolhida, de acordo com os fatores
# de conversão da tabela abaixo
# Moeda Valor (R$)
# Dólar americano 3,258
# Euro 4,095
# Libra esterlina 4,529
# Yuan 0,515

moeda = int(input("Digite o número da moeda que você quer fazer a conversão\n1-Dólar americano\n2-Euro\n3-Libra esterlina\n4-Yuan\n"))
valor = float(input("Digite o custo da operação em reais: "))

dolar = 3.258
euro = 4.095
libra = 4.529
yuan = 0.515

if moeda == 1: #dólar
    print("O valor convertido é de", valor*dolar, "dólares")
elif moeda == 2: #euro
    print("O valor convertido é de", valor*euro, "euros")
elif moeda == 3: #libra
    print("O valor convertido é de", valor*libra, "libras")
elif moeda == 4: #yuan
    print("O valor convertido é de", valor*yuan, "yuans")
else:
    print("Selecione uma das moedas para fazer a conversão")