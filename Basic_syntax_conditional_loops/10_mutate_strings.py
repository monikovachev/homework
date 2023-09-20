word1 = input()
word2 = input()
last_printed = word1

for character in range(len(word1)):
    left_part = word2[:character + 1]
    right_part = word1[character + 1:]
    new_word = left_part + right_part

    if new_word != last_printed:
        print(new_word)
        last_printed = new_word

