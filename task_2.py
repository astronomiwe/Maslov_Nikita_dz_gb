odd_cubed_numbers = []
total = 0


# функция определяет, делится ли сумма цифр первого аргумента на второй аргумент без остатка
def is_divide(dividend: int, denominator: int):
    digits_sum = 0
    while dividend > 0:
        digits_sum += dividend % 10
        dividend = dividend // 10
    return True if digits_sum % denominator == 0 else False


for i in range(1, 1000, 2):  # начинаем с 1 с шагом 2 - это и будут нечетные числа
    cubed_i = i ** 3
    odd_cubed_numbers.append(cubed_i)
    if is_divide(cubed_i, 7):  # вычисляем сразу, чтобы два раза не проходить по списку
        total += cubed_i

print('Массив кубов нечетных чисел от 1 до 1000:\n'
      f'{odd_cubed_numbers}')
print(f'Сумма всех чисел массива, сумма цифр которых делится на 7:  {total}')

total = 0  # обнуляем счетчик

print('Прибавляем к каждому элементу массива 17:')
for i in range(len(odd_cubed_numbers)):
    odd_cubed_numbers[i] += 17
    if is_divide(odd_cubed_numbers[i], 7):
        total += odd_cubed_numbers[i]

print(f'{odd_cubed_numbers}')
print(f'сумма всех чисел обновленного массива, сумма цифр которых делится на 7:  {total}')
