phonebook = {}

while True:
    entry = input()
    if '-' not in entry:
        break
    name, number = entry.split('-')
    phonebook[name] = number

for searched_contact in range(int(entry)):
    contact = input()
    if contact not in phonebook.keys():
        print(f'Contact {contact} does not exist.')
    else:
        print(f'{contact} -> {phonebook[contact]}')
