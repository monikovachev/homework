given_words = input().split()

odd_counts = {}

for word in given_words:
    word_lower = word.lower()
    if word_lower not in odd_counts:
        odd_counts[word_lower] = 0
    odd_counts[word_lower] += 1

for key, value in odd_counts.items():
    if value % 2 != 0:
        print(key, end=' ')
