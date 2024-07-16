""'''3. Escreva um programa com uma função que, dado um número inteiro (n > 1), retorne
uma lista com os fatores primos de n.
'''

def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

# numero de entrada do usuario
numero=int(input('insira um numero para descobrir os fatores primos dele: '))
print(fatores_primos(numero))  # Saída: 
