integer_list = []
rounded_list = []
mylist = input().split()
for num in mylist:
    integer_list.append(float(num))

for num in integer_list:
    rounded_list.append(round(num))

print(rounded_list)

