words = ['процент', 'процента', 'процентов']
user_input = int(input('Введите целое число процентов: '))


def print_percents(number, arr):
    # все числа с 11 до 20 будут склоняться "процентов"
    if number in range(11, 21):
        print(f'{number} {arr[2]}')
    # числа, оканчивающиеся на 1, кроме 11 (обработано выше) - 1, 21,31 и т.д. склоняются "процент"
    elif number % 10 == 1:
        print(f'{number} {arr[0]}')
    # числа, оканчивающиеся на 2,3,4 - 2,3,4,22,23,24 и т.д. склоняются "процента"
    elif 1 < number % 10 < 5:
        print(f'{number} {arr[1]}')
    # числа оканчивающиеся на 5-9 склоянются "процентов"
    elif number % 10 >= 5:
        print(f'{number} {arr[2]}')


print(f'Вы ввели число {user_input}. Результат:')
print_percents(user_input, words)

print('Проверяем склонения чисел от 1 до 20: ')
for numbers in range(1, 21):
    print_percents(numbers, words)
