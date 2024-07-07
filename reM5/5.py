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
lugares = [345, 345, 345, 345, 345, 345]

while True:
    print("-"*30)
    opcao = input("Selecione uma das opções:\n1-Lista de voos\n2-Fazer reserva\n3-Cancelar reserva\n4-Sair do programa\n")

    #Listar os voos
    if opcao == '1':
        print("-"*30)
        print("Os seguintes voos estão disponíveis:\n")

        for i in range(len(VOOS)):
            print(f"Voo {VOOS[i]}: {lugares[i]} lugares disponíveis")

        if input("Precione ENTER para voltar ao Menu") == "":
            continue
    
    #Fazer reserva
    if opcao == '2':
        print("-"*30)

        for i in range(len(VOOS)):
            print(f"Voo {VOOS[i]}: {lugares[i]} lugares disponíveis")

        reserva = input("Digite o número do voo que deseja fazer a reserva: ")
        if reserva in VOOS:
            #Salva o índice do voo em uma variável
            voo = VOOS.index(reserva)

            if lugares[voo] > 0:
                if input("Você deseja confirmar a reserva? [S/N]\n").lower() == "s":
                    lugares[voo] -= 1
                    print("-"*30)
                    print("Voo reservado com sucesso.")

                    if input("Precione ENTER para voltar ao Menu") == "":
                        continue

                else:
                    continue

            else:
                print("Não há lugares disponíveis neste voo.")
                if input("Precione ENTER para voltar ao Menu") == "":
                    continue

        else:
            print("-"*30)
            print("Não há nenhum voo com essa numeração. Por favor, verifique os voos disponíveis.")
            if input("Precione ENTER para voltar ao Menu") == "":
                continue

    #Cancelar reserva
    if opcao == '3':
        print("-"*30)
        
        # print(f'Voo {VOOS[0]}: {lugares[0]} lugares disponíveis\nVoo {VOOS[1]}: {lugares[1]} lugares disponíveis\nVoo {VOOS[2]}: {lugares[2]} lugares disponíveis\nVoo {VOOS[3]}: {lugares[3]} lugares disponíveis\nVoo {VOOS[4]}: {lugares[4]} lugares disponíveis\nVoo {VOOS[5]}: {lugares[5]} lugares disponíveis\n')
        for i in range(len(VOOS)):
            print(f"Voo {VOOS[i]}: {lugares[i]} lugares disponíveis")
        
        desf_reserva = input("Digite o número do voo que deseja cancelar a reserva: ")
        if desf_reserva in VOOS:
            #Salva o índice do voo em uma variável
            voo = VOOS.index(desf_reserva)

            if lugares[voo] < 345:
                if input("Você deseja cancelar a reserva? [S/N]\n").lower() == "s":
                    lugares[voo] += 1
                    print("-"*30)
                    print("Reserva cancelada com sucesso.")

                    if input("Precione ENTER para voltar ao Menu") == "":
                        continue

                else:
                    continue

            else:
                print("-"*30)
                print("Não há reservas neste voo.")
                if input("Precione ENTER para voltar ao Menu") == "":
                    continue

        else:
            print("-"*30)
            print("Não há nenhum voo com essa numeração. Por favor, verifique os voos disponíveis.")
            if input("Precione ENTER para voltar ao Menu") == "":
                continue

    if opcao == '4':
         print("-"*30)
         if input("Você deseja sair do programa? [S/N]\n").lower() == "s":
             break
         else:
             continue