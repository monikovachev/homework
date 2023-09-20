groups = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
for _ in range(groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        group1 += people_in_group
    elif people_in_group <= 12:
        group2 += people_in_group
    elif people_in_group <= 25:
        group3 += people_in_group
    elif people_in_group <= 40:
        group4 += people_in_group
    else:
        group5 += people_in_group

total = group1 + group2 + group3 + group4 + group5

print(f'{group1 / total * 100:.2f}%\n'
      f'{group2 / total * 100:.2f}%\n'
      f'{group3 / total * 100:.2f}%\n'
      f'{group4 / total * 100:.2f}%\n'
      f'{group5 / total * 100:.2f}%')

