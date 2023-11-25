text = input()
digits = ''
chrs = ''
others = ''
for chr in text:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        chrs += chr
    else:
        others += chr

print(f'{digits}\n{chrs}\n{others}')

