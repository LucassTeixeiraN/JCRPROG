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
    if menu.isdigit():
        menu = int(menu)

        if menu == 1:
            print("Lista de voos previstos:")
            for i in range(len(VOOS)):
                print("- voo", VOOS[i], "Assentos disponíveis:", assentos[i])
        if menu == 2:
            reserva = input(f"Em qual voo você deseja fazer uma reserva: \n1- 727({assentos[0]} lugares disponíveis)\n2- 442({assentos[1]} lugares disponíveis)\n3- 331({assentos[2]} lugares disponíveis)\n4- 447({assentos[3]} lugares disponíveis)\n5- 221({assentos[4]} lugares disponíveis)\n6- 291({assentos[5]} lugares disponíveis)\n")
            
            if reserva.isdigit():

                reserva = int(reserva)

                if reserva == 1:
                    if assentos[0] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[0] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                if reserva == 2:
                    if assentos[1] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[1] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                if reserva == 3:
                    if assentos[2] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[2] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                if reserva == 4:
                    if assentos[3] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[3] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                if reserva == 5:
                    if assentos[4] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[4] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                if reserva == 6:
                    if assentos[5] > 0:
                        confirmacao = input("Você deseja confirmar a reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[5] -= 1
                                print("Sua reserva foi feita com sucesso!")
                            else:
                                continue
                        else:
                            continue
        if menu == 3:
            desf_reserva = input(f"Em qual voo você deseja desfazer uma reserva: \n1- 727({assentos[0]} lugares disponíveis)\n2- 442({assentos[1]} lugares disponíveis)\n3- 331({assentos[2]} lugares disponíveis)\n4- 447({assentos[3]} lugares disponíveis)\n5- 221({assentos[4]} lugares disponíveis)\n6- 291({assentos[5]} lugares disponíveis)\n")
            
            if desf_reserva.isdigit():

                desf_reserva = int(desf_reserva)

                if desf_reserva == 1:
                    if assentos[0] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[0] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                elif desf_reserva == 2:
                    if assentos[1] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[1] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                elif desf_reserva == 3:
                    if assentos[2] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[2] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                elif desf_reserva == 4:
                    if assentos[3] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[3] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                elif desf_reserva == 5:
                    if assentos[4] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[4] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
                elif desf_reserva == 6:
                    if assentos[5] < 345:
                        confirmacao = input("Você deseja desfazer sua reserva \n1-Sim \n2-Não\n")
                        if confirmacao.isnumeric():
                            confirmacao = int(confirmacao)
                            if confirmacao == 1:
                                assentos[5] += 1
                                print("Sua reserva foi desfeita com sucesso!")
                            else:
                                continue
                        else:
                            continue
        if menu == 4:
            break

    else:
        print("Escolha uma das opções dadas anteriormente")