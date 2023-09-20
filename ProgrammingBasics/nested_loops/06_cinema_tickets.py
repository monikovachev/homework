movie_name = input()
total_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0

while not movie_name == 'Finish':
    capacity = int(input())
    type_ticket = input()
    total_tickets_movie = 0
    while True:

        if type_ticket == 'End':
            break

        if type_ticket == 'student':
            student_count += 1
        elif type_ticket == 'standard':
            standard_count += 1
        elif type_ticket == 'kid':
            kid_count += 1

        total_tickets_movie += 1
        total_tickets += 1
        if capacity <= total_tickets_movie:
            break

        type_ticket = input()
    print(f'{movie_name} - {total_tickets_movie / capacity * 100 :.2f}% full.')
    movie_name = input()

print(f'Total tickets: {total_tickets}')
print(f'{student_count / total_tickets * 100 :.2f}% student tickets.')
print(f'{standard_count / total_tickets * 100 :.2f}% standard tickets.')
print(f'{kid_count / total_tickets * 100 :.2f}% kids tickets.')

