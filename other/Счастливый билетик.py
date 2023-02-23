# Проверка на "счастливый" билетик" )))

# создаем список из цифр номера
ticket = list(map(int, input()))

# сумма первых трёх цифр
sum_left = sum(ticket[:-3])

# сумма последних трёх цифр
sum_right = sum(ticket[-3:])

print('YES' if sum_left == sum_right else 'NO')
