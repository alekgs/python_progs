
# command = '/show 25.09.2022 26.09.2022 27.09.2022 28.09.2022 29.09.2022 30.09.2022'
# command = command.removeprefix('/show')
# split_cmd = command.split()
# for date in split_cmd:
#     print(date)

# dictionary = {}
# key = "another_key"
# value = "another_value"
# dictionary["key"] = value
# dictionary[key] = value
# result = dictionary[key]
# print(result)

#
monitor1 = int(input())
sys_block1 = int(input())
keyboard1 = int(input())
mouse1 = int(input())

monitor2 = int(input())
sys_block2 = int(input())
keyboard2 = int(input())
mouse2 = int(input())

monitor3 = int(input())
sys_block3 = int(input())
keyboard3 = int(input())
mouse3 = int(input())

sum_monitor = monitor1 + monitor2 + monitor3
sum_sys_block = sys_block1 + sys_block2 + sys_block3
sum_keyboard = keyboard1 + keyboard2 + keyboard3
sum_mouse = mouse1 + mouse2 + mouse3

sum_itog = sum_monitor + sum_sys_block + sum_keyboard + sum_mouse

print(sum_itog)
