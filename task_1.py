
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24
SECONDS_IN_MONTH = SECONDS_IN_DAY * 30  # возьмем 30 дней за календарный месяц
SECONDS_IN_YEAR = SECONDS_IN_MONTH * 12

duration = int(input('Введите продолжительность времени в секундах: '))

if duration <= 0:
    print('количество секунд должно быть больше нуля')
else:
    #  хотелось бы как-то лаконичнее написать нижеследующий код (строки 14-24), но пока не представляю как
    years = duration // SECONDS_IN_YEAR
    duration = duration % SECONDS_IN_YEAR
    months = duration // SECONDS_IN_MONTH
    duration = duration % SECONDS_IN_MONTH
    days = duration // SECONDS_IN_DAY
    duration = duration % SECONDS_IN_DAY
    hours = duration // SECONDS_IN_HOUR
    duration = duration % SECONDS_IN_HOUR
    minutes = duration // SECONDS_IN_MINUTE
    duration = duration % SECONDS_IN_MINUTE
    seconds = duration

    if years > 0:
        print('{} лет {} месяцев {} дней {} часов {} мин {} сек'.format(years, months, days, hours, minutes, seconds))
    elif months > 0:
        print('{} месяцев {} дней {} часов {} мин {} сек'.format(months, days, hours, minutes, seconds))
    elif days > 0:
        print('{} дней {} часов {} мин {} сек'.format(days, hours, minutes, seconds))
    elif hours > 0:
        print('{} часов {} мин {} сек'.format(hours, minutes, seconds))
    elif minutes > 0:
        print('{} мин {} сек'.format(minutes, seconds))
    else:
        print(f'{seconds} сек')
