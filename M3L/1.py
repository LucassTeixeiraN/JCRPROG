# Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
# valor até R$100,00 ganha um cupom para concorrer a um carro e se ele comprar
# acima de R$100,00 ganha dois cupons e um vale-desconto no total de 10% da
# compra. Faça um programa que leia do teclado o total de compras e imprima se o
# cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
# o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
# desconto

limite = 100.0 
percentual_de_desconto = 0.1
valor_compra = float(input("Insira o valor da compra: "))
desconto = valor_compra*percentual_de_desconto

if valor_compra <= limite:
    print("Você ganhou um cupom para concorrer a um carro")
else:
    print("você ganhou dois cupons para concorrer a um carro e um vale-desconto de R$", desconto)