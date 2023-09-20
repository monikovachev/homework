V = float(input())
P1 = float(input())
P2 = float(input())
H = float(input())

total_fill = (P1 + P2) * H
p1 = P1 * H
p2 = P2 * H
p1_percent = p1 / total_fill * 100
p2_percent = p2 / total_fill * 100

total_percentage = total_fill / V * 100

if total_fill > V:
    print(f'For {H:.2f} hours the pool overflows with {abs(total_fill - V):.2f} liters.')
else:
    print(f'The pool is {total_percentage:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.')