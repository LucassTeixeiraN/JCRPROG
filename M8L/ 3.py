""'''3. Escreva um programa com uma função que, dado um número inteiro (n > 1), retorne
uma lista com os fatores primos de n.
'''
# Função para calcular os fatores primos de um número
def fatores_primos(n):
    fatores = []  # Lista para armazenar os fatores primos
    divisor = 2  # Começa com o menor número primo
    while n > 1:  # Continua até que n seja reduzido a 1
        while n % divisor == 0:  # Verifica se o divisor atual é um fator de n
            fatores.append(divisor)  # Adiciona o divisor à lista de fatores
            n //= divisor  # Divide n pelo divisor
        divisor += 1  # Incrementa o divisor para verificar o próximo número
    return fatores  # Retorna a lista de fatores primos

# Função principal para obter a entrada do usuário e exibir os fatores primos
def main():

# numero de entrada do usuario
    while True:
        try:
            numero = int(input('insira um numero para descobrir os fatores primos dele: '))
            print(fatores_primos(numero))  # Exibe os fatores primos do número
        except ValueError:
            print("Valores invalidos!")  # Mensagem de erro para entradas não inteiras

# Chama a função principal se o script for executado diretamente
main()
