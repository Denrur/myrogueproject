from random import randint

# на вход получаем номер уровня подземелья и таблицу значений, содержащих
# данные в формате [число, уровень]("вес предмета" и уровень на котором он
# появится), реверсируем таблицу, и для каждого
# значения в таблице сравниваем уровень подземелья с уровнем из таблицы. Если
# уровень подземелья больше, возвращаем число из таблицы, если меньше
# - возвращаем 0
def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value

    return 0

# Выбор рандомного индекса
def random_choice_index(chances):
    # Выбираем рандомное число из диапазона от 1 до суммы всех значений списка
    # переданного функции(рандомный шанс)
    random_chance = randint(1, sum(chances))
    print('Chances, Random_chance and sum(chances)')
    print(chances)
    print(random_chance)
    print(sum(chances))
    # текущая сумма равно 0
    running_sum = 0
    # Выбор равен 0
    choice = 0
    # Для каждого элемента списка chances
    for w in chances:
        print(w)
        # Увеличиваем текущую сумму на значение объекта из списка
        running_sum += w
        print(running_sum)
        # Если рандомный шанс меньше текущей суммы то возвращаем значение
        # choice, если нет - увеличиваем choice на 1
        if random_chance <= running_sum:
            return choice
        choice += 1

# Рандомный выбор из списка
def random_choice_from_dict(choice_dict):
    print('Choice dict')
    print(choice_dict)
    # Список вариантов
    choices = list(choice_dict.keys())
    # Список вероятностей
    chances = list(choice_dict.values())
    print('Choices, chances')
    print(choices)
    print(chances)
    # Возвращаем объект списка с рандомно выбранным индексом
    return choices[random_choice_index(chances)]
