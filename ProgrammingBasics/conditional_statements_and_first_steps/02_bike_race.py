junior_riders = int(input())
senior_riders = int(input())
path = input()

path_junior = [5.50, 8, 12.25, 20] # price for junior riders - trail, cross-country, downhill, road
path_senior = [7, 9.50, 13.75, 21.50] # price for senior riders - trail, cross-country, downhill, road
tax = 0

if path == 'trail':
    tax = junior_riders * path_junior[0] + senior_riders * path_senior[0]
elif path == 'cross-country':
    if junior_riders + senior_riders >= 50:
        tax = junior_riders * path_junior[1] + senior_riders * path_senior[1]
        tax = tax - tax * 0.25
    else:
        tax = junior_riders * path_junior[1] + senior_riders * path_senior[1]
elif path == 'downhill':
    tax = junior_riders * path_junior[2] + senior_riders * path_senior[2]
else:
    tax = junior_riders * path_junior[3] + senior_riders * path_senior[3]

tax = tax - tax * 0.05
print(f'{tax:.2f}')
