word = input().split()
for words in word:
    print(f'{words * len(words)}', end='')
