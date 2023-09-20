reptiles = ['crocodile', 'tortoise', 'snake']
mammal = ['dog']

animal = input()

if animal in reptiles:
    print('reptile')
elif animal in mammal:
    print('mammal')
else:
    print('unknown')
    