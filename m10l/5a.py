def hanoi(disc, ori, dest, aux):
    if disc == 1:
        print(f"Move disc {disc} from tower {ori} to the tower {dest}")
        return
    hanoi(disc - 1, ori, aux, dest)
    print(f"Move disc {disc} from tower {ori} to the tower {dest}")
    hanoi(disc - 1, aux, dest, ori)

# Exemplo de uso:
n = int(input("Digite o número de discos: "))
hanoi(n, 'A', 'C', 'B')
