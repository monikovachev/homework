pens_pack = 5.80
marker_pack = 7.20
detergent_per_litre = 1.20

pens_number = int(input())
marker_number = int(input())
detergent_number = int(input())
percent_discount = int(input()) / 100

total_sum = (pens_pack * pens_number)\
            + (marker_pack * marker_number)\
            + (detergent_per_litre * detergent_number)

total_sum_discount = total_sum - total_sum * percent_discount

print(total_sum_discount)