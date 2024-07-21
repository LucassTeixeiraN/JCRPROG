'''4. Implemente um programa com uma função para calcular o número de combinações
possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de
combinação:
    𝑚!
___________
(𝑚 − 𝑛)! 𝑛!
'''

# Calcula o fatorial de um número. 
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, num+1):
            fatorial *= i
        return fatorial

# Calcula o número de combinações possíveis de m elementos em grupos de n elementos usando a fórmula de combinação
def combinacoes(m, n):
    return fatorial(m) // (fatorial(m - n) * fatorial(n))

def main():
    print("-"*60)
    while True:
        try:
            m = int(input("Digite o valor de m: "))
            n = int(input("Digite o valor de n: "))
            if n <= m:
                print(f"\nO número de combinações possíveis de {m} elementos em grupos de {n} elementos é: {combinacoes(m, n)}")
            else:
                print("\nn deve ser menor ou igual a m.")
            print("-"*60)
        except ValueError:
            print("Valor inválido")

main()
