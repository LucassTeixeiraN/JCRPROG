'''4. Implemente um programa com uma função para calcular o número de combinações
possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de
combinação:
    𝑚!
___________
(𝑚 − 𝑛)! 𝑛!
'''
def fatorial(n,m):


    nf = n
    j = n

    mf = m
    x = m

    L = m-n
    Lf = L
    l = L

    lista = []
    for i in range(n):
        j -=1
        if j > 0:
            nf = nf * j
    for i in range(m):
        x -=1
        if x > 0:
            mf = mf * x
    for i in range(L):
        l -=1
        if l > 0:
            Lf = Lf * l
    result = mf/((Lf)*nf)
    return result
