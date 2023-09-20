coin_1 = int(input())
coin_2 = int(input())
bill_5 = int(input())
total = int(input())

for c1 in range(0, coin_1 + 1):
    for c2 in range(0, coin_2 + 1):
        for billy in range(0, bill_5 + 1):

            if ((c1 * 1) + (c2 * 2) + (billy * 5)) == total:
                print(f"{c1} * 1 lv. + {c2} * 2 lv. + {billy} * 5 lv. = {total} lv."
)

