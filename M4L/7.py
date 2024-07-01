# Uma indústria de alimentos congelados tem capacidade para estocar até 5 toneladas
# de produto pronto para venda. Faça um programa que controle o estoque dessa
# empresa, lendo do teclado a produção em kg de cada dia (sendo que uma produção
# igual a zero é utilizada para encerrar a leitura).

capacidade = 5000
dia = 0

while capacidade > 0:
    producao = float(input("Insira a produção de hoje em kg (Digite 0 para encerrar a leitura): "))
    if producao == 0:
        print("Leitura encerrada")
        break

    capacidade -= producao
    if(capacidade > 0):
        dia += 1
        print("Dia", dia, "\nO estoque ainda pode armazenar", capacidade, "kg")
    else:
        print("O estoque não tem capacidade para armazenar mais produtos")
