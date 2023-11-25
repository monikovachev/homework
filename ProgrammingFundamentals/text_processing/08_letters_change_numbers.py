import re
text = input().split()
total_sum = 0

numbers = [a for a in range(1, 27)]
alphabet_letters = [chr(letter) for letter in range(97, 123)]
alphabet = dict(zip(alphabet_letters, numbers))

for string in text:
    number = int(*re.findall(r'\d+', string))
    for char in string:
        if char.isalpha():
            if char == string[0]:
                if char.islower():
                    total_sum += number * alphabet[char.lower()]
                else:
                    total_sum += number / alphabet[char.lower()]
            else:
                if char.islower():
                    total_sum += alphabet[char.lower()]
                else:
                    total_sum -= alphabet[char.lower()]

print(f'{total_sum:.2f}')

# def calculate_number(pre_letter: str, post_letter: str, number: int) -> float:
#     if pre_letter.isupper():
#         def pre_operation(x): return x / (ord(pre_letter) - 64)
#     else:
#         def pre_operation(x): return x * (ord(pre_letter) - 96)
#
#     if post_letter.isupper():
#         def post_operation(x): return x - (ord(post_letter) - 64)
#     else:
#         def post_operation(x): return x + (ord(post_letter) - 96)
#     return post_operation(pre_operation(number))
#
#
# game_elements = input().split()
# result = 0
# for element in game_elements:
#     first_letter = element[0]
#     last_letter = element[-1]
#     middle_number = int(element[1:-1])
#     result += calculate_number(first_letter, last_letter, middle_number)
#
# print(f"{result:.2f}")