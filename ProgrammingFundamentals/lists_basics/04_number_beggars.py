given_string = input().split(', ')
beggars_count = int(input())
string_as_integers = []
outcome = []
sum_beggar = 0

for money in given_string:
    string_as_integers.append(int(money))

starting_index = 0

for beggar in range(beggars_count):
    sum_beggar = 0

    for index in range(starting_index, len(string_as_integers), beggars_count):
        sum_beggar += string_as_integers[index]

    starting_index += 1
    outcome.append(sum_beggar)

print(outcome)
