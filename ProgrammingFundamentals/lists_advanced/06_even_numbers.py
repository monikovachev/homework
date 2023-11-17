def even_numbers_indices():

    numbers_list = list(map(int, input().split(', ')))

    indices_list = list(map(lambda number: number if numbers_list[number] % 2 == 0 else None, range(len(numbers_list))))
    final_list = [number for number in indices_list if number is not None]
    return final_list


print(even_numbers_indices())
