n = int(input())
word = input()
mylist = []

for _ in range(n):

    given_string = input()
    mylist.append(given_string)

print(mylist)

for i in range(len(mylist) - 1, -1, -1):
    element = mylist[i]
    if word not in element:
        mylist.remove(element)

print(mylist)
