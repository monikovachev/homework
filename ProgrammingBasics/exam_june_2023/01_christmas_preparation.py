wrapping_paper_price = 5.80
material_price = 7.20
glue_price = 1.20

count_wrapping_paper = int(input())
count_material = int(input())
count_glue = float(input())
percent_discount = int(input())

total = (wrapping_paper_price * count_wrapping_paper
        + material_price * count_material
        + glue_price * count_glue)

total_plus_discount = total - (total * (percent_discount / 100))

print(f'{total_plus_discount:.3f}')
