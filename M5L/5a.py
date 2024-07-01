# Uma companhia aérea mantém uma lista de voos previstos, identificados pelo
# número de voo e outra para a quantidade de lugares ainda disponíveis em cada voo.
# Cada avião leva um total de até 345 passageiros. Faça um programa que:
# a. Inicialize a lista de voos para os valores 727, 442, 331, 447, 221, 291, inicialize a
# lista de lugares disponíveis para o valor máximo,
# b. Mostre um menu com as seguintes opções: listar voos previstos, fazer
# reserva, cancelar reserva e sair do programa.
# c. Faça reservas, indicando se ainda existem lugares disponíveis no voo citado.
# Se houver, o programa deve perguntar se o usuário quer confirmar a reserva.
# Se quiser, o número de lugares disponíveis para aquele voo deve ser
# decrementado.
# d. Desfaça reservas, incrementado o número de lugares disponíveis no voo
# correspondente.

VOOS = ('727', '442', '331', '447', '221', '291')
assentos = [345, 345, 345, 345, 345, 345]

while True:

    menu = input("Escolha a opção desejada: \n 1- Listar voos previstos. \n 2- Fazer reserva. \n 3- Cancelar reserva. \n 4- Sair do programa. \n Digite o valor correspondente a sua opção:\n")
    
    #verifica o se o input é válido
    if menu.isdigit() and 5 > int(menu) > 0:
        menu = int(menu)

        if menu == 1:
            print('-'*12)
            print("Lista de voos previstos:")
            for i in range(len(VOOS)):
                print("- voo", VOOS[i], "assentos disponíveis:", assentos[i])
            print('-'*12)

        if menu == 2:
            reserva = input(f"Em qual voo você deseja fazer uma reserva (digite o número do voo): \n727({assentos[0]} lugares disponíveis)\n442({assentos[1]} lugares disponíveis)\n331({assentos[2]} lugares disponíveis)\n447({assentos[3]} lugares disponíveis)\n221({assentos[4]} lugares disponíveis)\n291({assentos[5]} lugares disponíveis)\n")
            
            if reserva in VOOS:
                index_voo = VOOS.index(reserva)
                if assentos[index_voo] > 0:
                    confirmacao = input("Você deseja confirmar a reserva [S/N] ")
                    if confirmacao.lower() == "s":
                        assentos[index_voo] -= 1
                        print("Sua reserva foi feita com sucesso!")
                    else:
                        continue
                else:
                    print("Não há assentos disponíveis")
            else:
                print("Selecione um dos voos disponíveis")

        if menu == 3:
            desf_reserva = input(f"Em qual voo você deseja desfazer uma reserva (digite o número do voo): \n727({assentos[0]} lugares disponíveis)\n442({assentos[1]} lugares disponíveis)\n331({assentos[2]} lugares disponíveis)\n447({assentos[3]} lugares disponíveis)\n221({assentos[4]} lugares disponíveis)\n291({assentos[5]} lugares disponíveis)\n")
            
            if desf_reserva in VOOS:
                index_voo = VOOS.index(desf_reserva)
                if assentos[index_voo] < 345:
                    confirmacao = input("Você deseja desfazer a reserva? [S/N] ")
                    if confirmacao.lower() == "s":
                        assentos[index_voo] += 1
                        print("Sua reserva foi cancelada com sucesso!")
                    else:
                        continue
                else:
                    print("Não há reservas para esse voo")
            else:
                print("Selecione um dos voos disponíveis")
           
        if menu == 4:
            break

    else:
        print("Escolha uma das opções dadas anteriormente")