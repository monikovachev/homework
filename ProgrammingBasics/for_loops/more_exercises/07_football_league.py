capacity_stadium = int(input())
all_fans = int(input())
A_total = 0
B_total = 0
V_total = 0
G_total = 0

for _ in range(all_fans):
    sector = input()
    if sector == 'A':
        A_total += 1
    elif sector == 'B':
        B_total += 1
    elif sector == 'V':
        V_total += 1
    else:
        G_total += 1

print(f'{A_total / all_fans * 100:.2f}%')
print(f'{B_total / all_fans * 100:.2f}%')
print(f'{V_total / all_fans * 100:.2f}%')
print(f'{G_total / all_fans * 100:.2f}%')
print(f'{all_fans / capacity_stadium * 100:.2f}%')

