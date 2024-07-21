""'''3. Escreva um programa com uma função que, dado um número inteiro (n > 1), retorne
uma lista com os fatores primos de n.
'''
#Dentro do loop principal, temos um loop interno que verifica se n é divisível pelo divisor atual (n % divisor == 0).
#  Se for, adicionamos o divisor à lista fatores e dividimos n pelo divisor usando a divisão inteira (n //= divisor). 
# Este processo é repetido até que n não seja mais divisível pelo divisor atual.
def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

def main():

# numero de entrada do usuario
    while True:
        try:
            numero=int(input('insira um numero para descobrir os fatores primos dele: '))
            print(fatores_primos(numero))  # Saída: 
        except ValueError:

main()
