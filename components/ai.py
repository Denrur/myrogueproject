import tcod
from random import randint
from game_messages import Message

# Определяем поведение обычного монстра
class BasicMonster:
    # Определяем действия в ход монстра
    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        monster = self.owner
        # Если монстр находится в поле нашего зрения
        if tcod.map_is_in_fov(fov_map, monster.x, monster.y):
            # Если расстояние до монстра больше двух клеток
            if monster.distance_to(target) >= 2:
                # Монстр применяет алгоритм поиска пути A*
                monster.move_astar(target, entities, game_map)

            # Если монстр находится рядом и здоровье цели > 0, то монстр
            # атакует цель
            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)

        return results


# Поведение дезориентированого монстра
class ConfusedMonster:
    # на вход принимаем предыдущий ai и количество ходов в течении которых
    # монстр будет дезориентирован
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns
    # Определяем действия в ход дезориентированного монстра
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        # Если количество оставшихся ходов дезориентации больше 0
        if self.number_of_turns > 0:
            # Монстр передвигается в случайном направлении по вертикали и
            # горизонтали
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1

            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)
            #Уменьшаем количиство оставшихся ходов на 1
            self.number_of_turns -= 1
        else:
            # Если дезориентация закончилась, возвращаем монстра к предыдущей
            # модели поведения и выводим сообщение в лог
            self.owner.ai = self.previous_ai
            results.append({'message': Message('''The {0} is no longer
                                               confused!'''.format(
                                                   self.owner.name),
                                               tcod.red)})
        return results
