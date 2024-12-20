import timeit
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif a_list[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return False

#recursion
def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    elif a_list[midpoint] < item:
        return binary_search_recursive(a_list[midpoint + 1:], item)
    else:
        return binary_search_recursive(a_list[:midpoint], item)
print(binary_search_recursive([1 , 2, 3, 4, 5] , 6))

def binary_search_recursive_2(a_list, item):
    if len(a_list) == 0:
        return False
    mid_point = len(a_list) // 2
    if a_list[mid_point] == item:
        return True
    elif a_list[mid_point] < item:
        return binary_search_recursive_2(a_list[mid_point + 1])
# def ordered_sequential_search(a_list, item):
#     pos = 0
#     while pos < len(a_list):
#         if a_list[pos] == item:
#             return True
#         elif a_list[pos] > item:
#             return False
#         pos = pos + 1
#     return False

# # 测试开头、中间和结尾的搜索性能
# print("Binary Search (element at start):", timeit.timeit(lambda: binary_search(range(10000), 1), number=100))
# print("Binary Search (element at middle):", timeit.timeit(lambda: binary_search(range(10000), 5000), number=100))
# print("Binary Search (element at end):", timeit.timeit(lambda: binary_search(range(10000), 9999), number=100))

# print("Ordered Sequential Search (element at start):", timeit.timeit(lambda: ordered_sequential_search(range(10000), 1), number=100))
# print("Ordered Sequential Search (element at middle):", timeit.timeit(lambda: ordered_sequential_search(range(10000), 5000), number=100))
# print("Ordered Sequential Search (element at end):", timeit.timeit(lambda: ordered_sequential_search(range(10000), 9999), number=100))


