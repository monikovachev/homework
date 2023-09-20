men_count = int(input())
women_count = int(input())
max_tables = int(input())
tables_used = 0

for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        if tables_used >= max_tables:
            break

        print(f'({men} <-> {women})', end=' ')
        tables_used += 1



