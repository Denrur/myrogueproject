from random import randint


def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value

    return 0


def random_choice_index(chances):
    random_chance = randint(1, sum(chances))
    print('Chances, Random_chance and sum(chances)')
    print(chances)
    print(random_chance)
    print(sum(chances))

    running_sum = 0
    choice = 0
    for w in chances:
        print(w)
        running_sum += w
        print(running_sum)

        if random_chance <= running_sum:
            return choice
        choice += 1


def random_choice_from_dict(choice_dict):
    print('Choice dict')
    print(choice_dict)
    choices = list(choice_dict.keys())
    chances = list(choice_dict.values())
    print('Choices, chances')
    print(choices)
    print(chances)

    return choices[random_choice_index(chances)]
