"""
def get_div(n):
    res = {1, n}
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            res.add(d)
    return sorted(res)
"""

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}
# result = {i: get_div(i) for i in numbers}
print(result)
