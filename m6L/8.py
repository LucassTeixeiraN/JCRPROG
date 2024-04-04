# Faça um editor de texto usando uma matriz, que forneça as seguintes funções:
# a. O texto do usuário deve ser lido até que uma linha em branco seja digitada.
# b. O usuário pode reimprimir seu texto digitando i.
# c. O usuário pode trocar duas linhas de lugar digitando t onde o editor pergunta
# os números das linhas a serem trocadas entre si.
# d. O usuário pode redigitar uma linha digitando r, onde o editor pergunta o
# número da linha a ser redigitada.
# e. O usuário pode sair do editor digitando s.
# f. Se o usuário digitar um comando que não se encaixe em nenhum caso acima,
# o editor avisa que o comando não existe. 

matriz = []

# loop que salva o texto do usuário em uma matriz
print("Digite seu texto aqui (Dê ENTER em uma linha vazia para finalizar o texto):")
while True:
    texto = input()
    linha = []

    if texto == "":
        break

    for i in range(len(texto)):
        linha.append(texto[i])
        
    matriz.append(linha)

# loop que verifica quais comandos o usuário está usando
while True:
    print("-"*15)
    comandos = input("Comandos:\ni- Reimprime o texto\nt- Troca duas linhas de lugar\nr- Redigita uma linha\ns- Sair do programa\n")
    print("-"*15)
    
    if comandos.lower() == "i":
        for i in range(len(matriz)):
            linha_str = ""
            for j in range(len(matriz[i])):
                linha_str += matriz[i][j]
            print(linha_str)
        if input("-"*15 + "\nPrecione ENTER para continuar") == "":
            continue

    elif comandos.lower() == "t":
        l1_inp = input("Digite a primeira linha que você deseja trocar de posição: ")
        l2_inp = input("Digite a segunda linha que você deseja trocar de posição: ")
        if l1_inp.isdigit() and l2_inp.isdigit:
            l1_inp = int(l1_inp)
            l2_inp = int(l2_inp)
            if l1_inp > 0 and l1_inp <= len(matriz) and l2_inp > 0 and l2_inp <= len(matriz):
                l1 = matriz[l1_inp-1]
                l2 = matriz[l2_inp-1]

                matriz[l1_inp - 1] = l2
                matriz[l2_inp - 1] = l1

            else:
                print("!!Essa linha não existe!!")
                continue
        else:
            print("!!Valor inválido!!")
            continue

    elif comandos.lower() == "r":
        linha_red = input("Digite a linha que deseja redigitar: ")
        if linha_red.isdigit():
            linha_red = int(linha_red)
            if linha_red > 0 and linha_red <= len(matriz):
                novo_texto = input("Digite o novo texto: ")
                matriz[linha_red - 1] = novo_texto
            else:
                print("!!Essa linha não existe!!")
                continue
        else:
            print("!!Valor inválido!!")
            continue

    elif comandos.lower() == "s":
        if input("Você deseja sair da aplicação? [S/N] ").lower() == "s":
            break
        else:
            continue

    else:
        print("!!Comando inválido, tente utilizar um dos comandos a baixo!!")
        continue