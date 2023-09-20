age = float(input())
sex = input()

if age >= 16:
    if sex == 'f':
        result = 'Ms.'
    else:
        result = 'Mr.'
else:
    if sex == 'f':
        result = 'Miss'
    else:
        result = 'Master'

print(result)