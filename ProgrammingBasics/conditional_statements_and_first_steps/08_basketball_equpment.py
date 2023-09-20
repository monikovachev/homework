tax_yearly = int(input())

basketball_shoe = tax_yearly - tax_yearly * 0.4
basketball_shorts = basketball_shoe - basketball_shoe * 0.2
basketball_ball = basketball_shorts * 0.25
basketball_accessories = basketball_ball * 0.2

sum_all = tax_yearly + basketball_accessories + basketball_ball + basketball_shorts + basketball_shoe

print(sum_all)