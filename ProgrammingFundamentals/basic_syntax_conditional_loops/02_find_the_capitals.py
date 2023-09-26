string = input()
result_list = []

for index, letter in enumerate(string):

    if letter.isupper():
        result_list += [index]

print(result_list)

# def capital_indexes(string):
#     return [i for i, char in enumerate(string) if char.isupper()]
#
# print(capital_indexes("HellO WoRlD"))