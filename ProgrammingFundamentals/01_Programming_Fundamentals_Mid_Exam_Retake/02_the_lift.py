people_q = int(input())
current_state_of_lift = input()

lift_list = current_state_of_lift.split(' ')

for index, wagon in enumerate(lift_list):

    wagon_capacity = int(wagon)
    while wagon_capacity < 4:
        wagon_capacity += 1
        people_q -= 1
        if people_q == 0:
            print(f'The lift has empty spots!\n{lift_list}')
            break

print(lift_list)