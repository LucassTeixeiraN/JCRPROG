'''4. Implemente um programa com uma função para calcular o número de combinações
possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de
combinação:
    𝑚!
___________
(𝑚 − 𝑛)! 𝑛!
'''
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

def combinacoes(m, n):
    return fatorial(m) // (fatorial(m - n) * fatorial(n))

def main():
    m = int(input("Digite o valor de m: "))
    n = int(input("Digite o valor de n: "))
    if n <= m:
        print(f"O número de combinações possíveis de {m} elementos em grupos de {n} elementos é: {combinacoes(m, n)}")
    else:
        print("Erro: n deve ser menor ou igual a m.")

if __name__ == "__main__":
    main()

