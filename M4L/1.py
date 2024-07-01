# A população americana, em um determinado ano, ultrapassa a população brasileira.
# No entanto, a taxa de crescimento aqui é de 4% ao ano e lá é de 2% ao ano. Faça um
# programa para calcular em que ano a população brasileira irá ultrapassar a
# americana

pop_americana = int(input('Insira a população americana: '))
pop_brasileira = int(input('Insira a população brasileira: '))
ano = int(input('Insira o ano atual: '))

while pop_americana > pop_brasileira:
    pop_brasileira += pop_brasileira * 0.04
    pop_americana += pop_americana * 0.02
    ano += 1

print("A população brasileira ultrapassará a americana em", ano)