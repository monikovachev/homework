sqm_all = float(input())

one_sqm_price = 7.61
discount_percent = 0.18

final_price = (sqm_all * one_sqm_price) - (sqm_all * one_sqm_price) * 0.18
discount_total = (sqm_all * one_sqm_price) * 0.18

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_total} lv.")