def loading_bar(number):

    loading_list = []
    percent_count = number // 10

    loading_list.append(percent_count * '%')

    if len(loading_list[0]) < 10:
        loading_list.append((10 - len(loading_list[0])) * '.')

    if loading_list[0].count('%') == 10:
        final_list = ''.join(loading_list)
        return f'100% Complete!\n[{final_list}]'
    final_list = ''.join(loading_list)
    return f'{number}% [{final_list}]\nStill loading...'


given_number = int(input())
print(loading_bar(given_number))

