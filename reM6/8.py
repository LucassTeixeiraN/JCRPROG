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

texto = []

print("Insira o texto (aperte ENTER em uma linha vazia para finalizá-lo):")
while True:
    linha = input()
    if linha == "":
        break


    texto.append(linha)


while True:
    print("-"*65)
    comando = input("Digite o caractér indicado para realizar cada ação:\ni - Reimprimir o texto\nt - Trocar duas linhas de lugar\nr - Redigitar uma linha\ns - Sair do editor:\n")

    if comando.lower() == "i":
        print("-"*65)
        for i in texto:
            print(i)

        if input("\nPressione ENTER para continuar") == "":
            continue

    elif comando.lower() == "t":
        print("-"*65)
        l1 = input("Digite o número da primeira linha a ser trocada: ")
        l2 = input("Digite o número da segunda linha a ser trocada: ")
        if l1.isdigit() and l2.isdigit() and 0 < int(l1) <= len(texto) and  0 < int(l2) <= len(texto):
            l1 = int(l1) - 1
            l2 = int(l2) - 1

            linha_guard = texto[l1]
            texto[l1] = texto[l2]
            texto[l2] = linha_guard
        else:
            print("-"*65)
            print("Essa linha não existe")
            if input("\nPressione ENTER para voltar para o Menu") == "":
                continue
    
    elif comando.lower() == "r":
        print("-"*65)
        l1 = input("Digite o número da linha a ser redigitada: ")

        if l1.isdigit() and 0 < int(l1) <= len(texto):
            l1 = int(l1) - 1
            linha = input("Digite o novo texto:\n")
            texto[l1] = linha
        else:
            print("-"*65)
            print("Essa linha não existe")
            if input("\nPressione ENTER para voltar para o Menu") == "":
                continue

    elif comando.lower() == "s":
        if input("Digite 's' se você realmente deseja sair da aplicação: ").lower() == "s":
            break
        else: 
            continue
    else:
        print("Este comando não existe")
        if input("\nPressione ENTER para continuar") == "":
            continue
