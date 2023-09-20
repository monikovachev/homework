current_leader = 0
while True:
    command = input()
    if command == 'END':
        break
    goals_scored = int(input())

    if goals_scored > current_leader:
        current_leader = goals_scored
        player = command
    if goals_scored >= 10:
        break

print(f'{player} is the best player!')
if current_leader >= 3:
    print(f'He has scored {current_leader} goals and made a hat-trick !!!')
else:
    print(f'He has scored {current_leader} goals.')
