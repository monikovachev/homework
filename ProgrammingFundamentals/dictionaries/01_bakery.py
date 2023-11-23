my_dict = {}

text = input().split()

for i in range(0, len(text), 2):
    food = text[i]
    quantity = int(text[i + 1])
    my_dict[food] = quantity

print(my_dict)
