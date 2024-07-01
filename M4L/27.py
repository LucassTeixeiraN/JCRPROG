# O custo de produção de um livro é constituído dos custos por página, mais o custo
# de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o
# custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo
# utilizada a seguinte tabela:
# • Encadernação simples: R$4,30
# • Encadernação especial: R$7,80
# • Encadernação luxo: R$10,50
# Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de
# encadernação e o número de vendas previstas (número de cópias) e:
# a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e
# o preço de venda para que a editora tenha um lucro de 20%.
# b. Imprima o total de livros analisados.
# c. Imprima o preço médio de venda dos livros (com lucro de 20%).
# d. Imprima o preço de venda dos livros mais barato e mais caro. 


custo_pagina = 0.03
custo_fixo = 4397
total_livros = preco_total = mais_barato = mais_caro = 0

while True:
    numero_pagina = int(input("Insira o número de página do livro (Insira 0 se não quiser mais adicionar livros): "))

    if numero_pagina == 0:
        break

    tipo_encadernacao = int(input("Insira o tipo de encadernação:\n1- Simples (R$ 4,30)\n2- Especial (R$ 7,80)\n3- Luxo (R$ 10,50)\n"))
    numero_vendas_previstas = int(input("Insira o número de vendas prevista para o produto: "))

    total_livros += 1

    if tipo_encadernacao == 1:
        preco_encadernacao = 4.3
    elif tipo_encadernacao == 2:
        preco_encadernacao = 7.8
    else:
        preco_encadernacao = 10.5


    custo = custo_fixo + (custo_pagina * numero_pagina) + preco_encadernacao
    preco_minimo = round((custo*1.2) / numero_vendas_previstas, 2)
    preco_total += preco_minimo
    print("O preço mínimo para cada livro (que cubra os custos e os 20% da editora) é de: R$", preco_minimo)

    if mais_barato == 0 or preco_minimo < mais_barato:
        mais_barato = preco_minimo
    
    if preco_minimo > mais_caro:
        mais_caro = preco_minimo

preco_medio = preco_total/total_livros

print("Total de livros analizados: ", total_livros, 
      "\nO preço médio dos livros é: R$ ", round(preco_medio, 2), 
      "\nO livro mais caro custou: R$ ", mais_caro, 
      "\nE o mais barato: R$ ", mais_barato, sep="")