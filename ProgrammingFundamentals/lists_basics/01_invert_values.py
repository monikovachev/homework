given_string = input()
mylist = given_string.split()
inverted_list = []

for number in mylist:
    inverted_list.append(-int(number))

print(inverted_list)