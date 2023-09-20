goal = 10000
has_reached = True
steps_count = 0
steps = 0

while steps_count < goal:
    steps = input()
    if steps == 'Going home':
        last_steps = int(input())
        steps_count += last_steps
        if steps_count < goal:
            has_reached = False
            break
        else:
            break

    steps_count += int(steps)

if has_reached:
    print(f'Goal reached! Good job!\n{steps_count - goal} steps over the goal!')
else:
    print(f'{goal - steps_count} more steps to reach goal.')
