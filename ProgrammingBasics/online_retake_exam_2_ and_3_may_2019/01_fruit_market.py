strawberry = float(input())
banana_count = float(input())
orange_count = float(input())
raspberry_count = float(input())
strawberry_count = float(input())

raspberry = strawberry * 0.50
orange = raspberry * 0.60
banana = raspberry * 0.20

total = strawberry * strawberry_count\
        + banana * banana_count\
        + orange * orange_count\
        + raspberry_count * raspberry

print(f'{total:.2f}')
