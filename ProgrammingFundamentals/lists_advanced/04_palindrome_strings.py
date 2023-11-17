words = input().split()
palindrome_given = input()

palindromes = [word for word in words if word[::-1] == word]
print(palindromes)
print(f'Found palindrome {palindromes.count(palindrome_given)} times')
