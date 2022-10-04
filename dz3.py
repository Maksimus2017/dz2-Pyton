# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:

number_n = int(input('Введите число N: '))
result_sequence = {}
sum_sequence = 0
for key in range(1, number_n+1):
    result_sequence[key] = round((1+1/key)**key, 2)
    sum_sequence += result_sequence[key]
print(f'n = {number_n}:{result_sequence} \ncумма= {round(sum_sequence,3)}')
