budget = float(input())
gpu_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

GPU_PRICE = 250
CPU_PRICE = (GPU_PRICE * gpu_quantity) * 0.35
RAM_PRICE = (GPU_PRICE * gpu_quantity) * 0.10

total_order = GPU_PRICE * gpu_quantity \
              + CPU_PRICE * cpu_quantity \
              + RAM_PRICE * ram_quantity

if gpu_quantity > cpu_quantity:
    total_order = total_order - total_order * 0.15

leftover = abs(budget - total_order)

if budget >= total_order:
    print(f'You have {leftover:.2f} leva left!')
else:
    print(f'Not enough money! You need {leftover:.2f} leva more!')
