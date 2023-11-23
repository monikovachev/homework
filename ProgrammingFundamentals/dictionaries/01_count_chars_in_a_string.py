given_text = input().split()
count_dict = {}

for word in given_text:
    for char in word:
        if char not in count_dict.keys():
            count_dict[char] = 0
        count_dict[char] += 1

for key, value in count_dict.items():
    print(f'{key} -> {value}')