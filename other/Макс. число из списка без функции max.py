max_num = 0
for i in range(int(input())):
    num = int(input())
    if max_num:
        if num > max_num:
            max_num = num
    else:
        max_num = num
print(max_num)
