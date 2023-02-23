# put your python code here
n = input('Введите число HEX: ')
len_hex = len(n)
abc = 'ABCDEF'
dec = 0
for i in range(len_hex):
    st = 16 ** (len(n) - (i + 1))
    if n[i].isdigit():
        dec += int(n[i]) * st
    else:
        dec += (10 + abc.index(n[i])) * st
print(dec)
