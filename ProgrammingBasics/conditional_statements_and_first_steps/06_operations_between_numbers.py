N1 = int(input())
N2 = int(input())
operator = input()

result = 0
type = ''

if operator == '+':
    result = N1 + N2
elif operator == '-':
    result = N1 - N2
elif operator == '*':
    result = N1 * N2
elif operator == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 / N2
else:
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 % N2

if result % 2 == 0:
    type = 'even'
else:
    type = 'odd'

if operator == '+' or operator == '-' or operator == '*':
    print(f'{N1} {operator} {N2} = {result} - {type}')
elif operator == '/' and N2 != 0:
    print(f'{N1} {operator} {N2} = {result:.2f}')
elif operator == '%' and N2 != 0:
    print(f'{N1} {operator} {N2} = {result}')



