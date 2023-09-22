# First option


# number = int(input())
#
# is_special = False
#
# while not is_special:
#     number += 1
#     number_string = str(number)
#
#     is_special = True
#     for digit in number_string:
#         if number_string.count(digit) != 1:
#             is_special = False
#             break
#
# print(number)


# Below using set function


year = int(input())

while True:
    year += 1

    year_string = str(year)

    if len(year_string) == len(set(year_string)):
        print(year)
        break

