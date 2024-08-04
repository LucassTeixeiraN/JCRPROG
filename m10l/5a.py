def hanoi(disc, ori, dest, aux):
    if disc == 1:
        print(f"Mova o disco {disc} da torre {ori} para a torre {dest}")
        return
    
    hanoi(disc - 1, ori, aux, dest)

    print(f"Mova o disco {disc} da torre {ori} para a torre {dest}")

    hanoi(disc - 1, aux, dest, ori)

def main():
    while True:
        try:
            n = int(input("Digite o número de discos: "))
            break
        except ValueError:
            print("Entrada invalida, digite numeros inteiros.")
            
    hanoi(n, 'A', 'C', 'B')
main()
