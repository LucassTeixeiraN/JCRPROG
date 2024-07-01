# O número 3025 possui a interessante característica:
# 30 + 25 = 55
# 55² = 3025
# Faça um programa que procure todos os números de 4 algarismos que possuem essa
# característica

# i = 2 primeiros algarismos
# j = 2 ultimos algarismos

for i in range(10, 100):
    i_str = str(i)

    for j in range(0, 100):
        j_str = str(j)
    
        number = i_str + j_str
        
        x = (i + j) ** 2

        if j >= 10:
            if x == int(number):
                print(number)
        else:
            if x == int(i_str+"0"+j_str):
                print(i_str+"0"+j_str)