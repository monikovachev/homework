period = int(input())
nurses = 7
treated = 0
untreated = 0

for _ in range(1, period + 1):
    patients = int(input())
    if _ % 3 == 0 and untreated > treated:
        nurses += 1

    if patients > nurses:
        untreated += patients - nurses
        treated += nurses
    else:
        treated += patients

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')

