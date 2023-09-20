actor_name = input()
points_from_academy = float(input())
number_of_judges = int(input())

total_points = points_from_academy

for _ in range(number_of_judges):
    name_of_judge = input()
    points_from_judge = float(input())
    total_points += len(name_of_judge) * points_from_judge / 2

    if total_points > 1250.5:
        break

if total_points < 1250.5:
    print(f'Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!')
else:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
