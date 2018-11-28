import tcod
from game_messages import Message


# Компонент, отвечающий за возможность наносить и получать урон
class Fighter:
    # Базовые характеристики - здоровье, защита, атака, опыт за убийство
    def __init__(self, hp, defense, power, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp
    # Свойство - максимальное здоровье у учетом бонусов от вещей
    @property
    def max_hp(self):
        # Проверяем, экипирован ли предмет с бонусом и прибавляем показатель
        # бонуса к базовой характеристике
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        # Проверяем, экипирован ли предмет с бонусом и прибавляем показатель
        # бонуса к базовой характеристике
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

    @property
    def defense(self):
        # Проверяем, экипирован ли предмет с бонусом и прибавляем показатель
        # бонуса к базовой характеристике
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    # Получение урона
    def take_damage(self, amount):
        results = []
        # Вычетаем из значения текущего здоровья значение нанесенного урона
        self.hp -= amount

        # Если здоровье падает ниже 0, персонаж умирает и отдает определенное
        # количество опыта
        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results
    # Лечение
    def heal(self, amount):
        self.hp += amount
        # Если текущее здоровье становится больше максимального здоровья,
        # приравниваем текущее к максимальнму
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    # Нанесение урона
    def attack(self, target):
        results = []

        # Урон равен значению атаки минус значение защиты цели
        damage = self.power - target.fighter.defense

        # Если урон больше 0
        if damage > 0:
            # Выводим сообщение в чат
            results.append({'message':
                            Message('{0} attacks {1} for {2} points.'.format(
                                self.owner.name.capitalize(),
                                target.name, str(damage)),
                                tcod.white)})
            # Добавляем в список результатов результаты получения урона целью
            results.extend(target.fighter.take_damage(damage))
        else:
            # Если урон меньше 0, выводим информацию об этом в лог
            results.append({'message':
                            Message('{0} attacks {1} but does no dmg.'.format(
                                self.owner.name.capitalize(),
                                target.name),
                                tcod.white)})

        return results
