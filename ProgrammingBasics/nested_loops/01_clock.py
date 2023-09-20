hour = 0
minutes = 0

while hour <= 23:
    for minutes in range(60):
        print(f'{hour}:{minutes}')
    hour += 1


#Solution 2, if minutes need to be formatted with 0 in front
# while hour <= 23:
#     for minutes in range(0, 60):
#         if minutes < 10:
#             print(f'{hour}:0{minutes}')
#         else:
#             print(f'{hour}:{minutes}')
#     hour += 1
