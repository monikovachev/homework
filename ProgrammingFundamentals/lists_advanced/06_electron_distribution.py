electrons_number = int(input())

shells = []

for shell in range(1, electrons_number + 1):

    max_electrons_in_shell = 2 * shell ** 2
    if electrons_number >= max_electrons_in_shell:
        shells.append(max_electrons_in_shell)
        electrons_number -= max_electrons_in_shell
        if electrons_number == 0:
            break
    else:
        shells.append(electrons_number)
        break

print(shells)


