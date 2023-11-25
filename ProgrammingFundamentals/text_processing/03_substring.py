text = input()
second_text = input()

while text in second_text:
    second_text = second_text.replace(text, '')
print(second_text)
 