facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

number_tabs = int(input())
salary = int(input())

for _ in range(number_tabs):
    page = input()
    if page == 'Facebook':
        salary -= facebook_fine
    elif page == 'Instagram':
        salary -= instagram_fine
    elif page == 'Reddit':
        salary -= reddit_fine

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(salary)
# else:  #18 row delete
#     print(f'You have lost your salary.')

