factor = int(input())
count = int(input())
step = factor
mylist = []

for number in range(count):
    mylist.append(factor)
    factor += step

print(mylist)



