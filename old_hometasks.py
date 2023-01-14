#_______________________1 ЗАДАНИЕ___________________________
def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    i = -1
    for travel in list(reversed(geo_logs)):
        for cities,countries in travel.items():
            if "Россия" not in countries:
                geo_logs.remove(geo_logs[i])
            else:
                i -= 1 
    return geo_logs
#_______________________2 ЗАДАНИЕ___________________________
def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    user_1 = set(ids['user1'])
    user_2 = set(ids['user2'])
    user_3 = set(ids['user3'])
    numbers = user_1 | (user_2.symmetric_difference(user_3))
    return numbers
# _________________________3 ЗАДАЧА____________________________
def task_3():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    return max(stats, key=stats.get)