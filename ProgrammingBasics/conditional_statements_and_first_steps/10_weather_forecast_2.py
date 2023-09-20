degrees = float(input())

if degrees > 35:
    print('unknown')
elif degrees < 5:
    print('unknown')

if degrees <= 11.9:
    print('Cold')
elif degrees <= 14.9:
    print('Cool')
elif degrees <= 20.0:
    print('Mild')
elif degrees <= 25.9:
    print('Warm')
elif degrees <= 35.0:
    print('Hot')