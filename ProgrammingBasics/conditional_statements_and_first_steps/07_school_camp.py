season = input()
group_gender = input()
students_count = int(input())
nights_stay = int(input())
sport = ''
price_nightly = 0

if season == 'Winter':
    if group_gender == 'boys':
        price_nightly = 9.60
        sport = 'Judo'
    elif group_gender == 'girls':
        price_nightly = 9.60
        sport = 'Gymnastics'
    else:
        price_nightly = 10
        sport = 'Ski'
elif season == 'Spring':
    if group_gender == 'boys':
        price_nightly = 7.20
        sport = 'Tennis'
    elif group_gender == 'girls':
        price_nightly = 7.20
        sport = 'Athletics'
    else:
        price_nightly = 9.50
        sport = 'Cycling'
else:
    if group_gender == 'boys':
        price_nightly = 15
        sport = 'Football'
    elif group_gender == 'girls':
        price_nightly = 15
        sport = 'Volleyball'
    else:
        price_nightly = 20
        sport = 'Swimming'

total_price = price_nightly * students_count * nights_stay

if 10 <= students_count < 20:
    total_price *= 0.95
elif 20 <= students_count < 50:
    total_price *= 0.85
elif students_count >= 50:
    total_price *= 0.50

print(f'{sport} {total_price:.2f} lv.')

