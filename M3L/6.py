# Um programa didático para crianças consiste em pedir dois números inteiros
# quaisquer para a criança e depois perguntar a soma desses dois números. Se a
# resposta estiver certa, o programa imprime uma mensagem de incentivo. Se não, o
# programa imprime o valor correto da soma. Implemente esse programa.

n1 = int(input("Insira um número inteiro qualquer "))
n2 = int(input("Insira outro número inteiro qualquer "))
soma = int(input("Insira a soma dos dois números anteriores "))

if n1 + n2 == soma:
    print(n1, "+", n2, "=", soma)
    print("Sabe muito")
else:
    print(n1, "+", n2, "=", n1+n2)
    print("Continue tentando")

