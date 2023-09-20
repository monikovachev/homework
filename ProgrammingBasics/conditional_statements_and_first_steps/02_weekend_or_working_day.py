day = input()
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if day in weekdays:
    print('Working day')
elif day in weekend:
    print('Weekend')
else:
    print('Error')

    