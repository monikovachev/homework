def characters_between(a, b):

    characters = []
    for character in range(ord(a) + 1, ord(b)):
        characters.append(chr(character))

    return characters


first_character = input()
second_character = input()

print(*characters_between(first_character, second_character))
