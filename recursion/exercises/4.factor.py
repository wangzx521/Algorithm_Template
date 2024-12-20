def calculate_factor(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factor(n - 1)
print(calculate_factor(5))