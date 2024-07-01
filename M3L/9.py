# O que acontece no programa anterior se a pessoa nasceu há 18 anos, mas ainda não
# fez aniversário? Melhore o programa para que, neste caso, o programa pergunte se a
# pessoa já fez aniversário ou não antes de imprimir o resultado. 

ano_atual = 2024
limite_de_maioridade = 18
ano_de_nascimento = int(input("Insira seu ano de nascimento "))

if ano_atual - ano_de_nascimento > 18:
    print("Maior de idade")
elif ano_atual - ano_de_nascimento == 18:
    fez_aniversario = int(input("Você já fez aniversário?:\n1-Sim\n2-Não\n"))
    if fez_aniversario == 1:
        print("Maior de idade")
    else:
        print("Menor de idade")
else:
    print("Menor de idade")
