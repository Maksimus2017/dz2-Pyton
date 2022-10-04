# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


float_number = float(input('Введите число: '))
num_sum = 0
if float_number < 0:
    float_number *= -1
float_str = str(float_number)
for i in float_str:
    if i != '.':
        num_sum += int(i)
print(num_sum)       