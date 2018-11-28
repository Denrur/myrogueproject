import tcod
from game_messages import Message


# Компонент определяющий параметры инвентаря персонажа
class Inventory:
    # Инициализация - вместимость инвентаря и пустой список для предметов
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    # Добавление предмета в инвентарь
    def add_item(self, item):
        # Пустой список результатов
        results = []
        # Если длина списка предметов больше либо равна вместимости инвентаря,
        # выводим сообщение в лог
        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message':
                Message('You cannot carry any more, your inventory is full',
                        tcod.yellow)
            })
        else:
            # Если нет - добалвяем предмет в список результатов, выводим
            # сообщение в лог
            results.append({
                'item_added': item,
                'message':
                Message('You pick up the {0}!'.format(item.name),
                        tcod.blue)
            })
            # Добавляем предмет в список предметов в инвентаре
            self.items.append(item)
        # Возвращаем список результатов
        return results
    # Использование предмета(item_entity) в инвентаре
    def use(self, item_entity, **kwargs):
        # Пустой список результатов
        results = []
        # Присваиваем переменной компоненту Item предмета item_entity
        item_component = item_entity.item
        # Если у предмета нет функции использования
        if item_component.use_function is None:
            # присваиваем переменной компоненту equippable предмета item_entity
            equippable_component = item_entity.equippable
            # Если у предмета есть такая компонента
            if equippable_component:
                # Добавляем в список результатов экипировку предмета
                results.append({'equip': item_entity})
            else:
                # Если у предмета нет ни функции использования ни функции
                # экипировки выводим в лог сообщение что этот предмет нельзя
                # использовать
                results.append({'message':
                                Message(
                                    'The {0} cannot be used'
                                    .format(item_entity.name),
                                    tcod.yellow)})
        # Если у предмета есть функция использования
        else:
            '''Проверяем, установлено ли значение компоненты targeting на True,
            а так же были ли получены переменные координат цели. Если нет, то
            мы можем предположить что цель еще не выбрана, и состояние игры
            нужно переключить на TARGETING.
            Если координаты получены, мы можем использовать объект
            '''
            # Если у предмета есть компонента targeting но нет координат цели
            if item_component.targeting and not(kwargs.get('target_x')
                                                or kwargs.get('target_y')):
                # добавляем предмет с пометкой targeting к списку результатов
                results.append({'targeting': item_entity})
            else:
                # Тут магия применения предмета
                kwargs = {**item_component.function_kwargs, **kwargs}
                item_use_results = item_component.use_function(self.owner,
                                                               **kwargs)
                # Если предмет помечен как примененный - удаляем предмет из
                # списка иневентаря
                for item_use_result in item_use_results:
                    if item_use_result.get('consumed'):
                        self.remove_item(item_entity)
                # Добавляем в список результатов результаты использования
                # предмета
                results.extend(item_use_results)

        return results
    # Удаление предмета
    def remove_item(self, item):
        self.items.remove(item)
    # Выбрасывание предмета из инвентаря
    def drop_item(self, item):
        # Пустой список результатов
        results = []
        # Если предмет экипирован, снимаем его
        if (self.owner.equipment.main_hand == item or
                self.owner.equipment.off_hand == item):
            self.owner.equipment.toogle_equip(item)

        # Координаты выброшенного предмета равны координатам персонажа, который
        # предмет выбросил
        item.x = self.owner.x
        item.y = self.owner.y
        # Удаляем предмет из инвентаря
        self.remove_item(item)
        # Добавляем к списку резултьтатов предмет с пометкой Выброшен, и
        # выводим сообщение в лог
        results.append({'item_dropped': item,
                        'message': Message('You dropped the {0}'.format(
                            item.name), tcod.yellow)})

        return results
