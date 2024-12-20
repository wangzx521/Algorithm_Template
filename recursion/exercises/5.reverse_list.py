def reverse_list(list):
    if len(list) == 1:
        return list
    else:
        return [list[-1]] + reverse_list(list[:-1])
print(reverse_list([1, 2, 3, 4, 5]))