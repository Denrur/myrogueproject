from equipment_slots import EquipmentSlots


class Equipment:
    # определяем переменные, которые будут содержать экипированые предметы. По
    # умолчанию ничего не экипировано
    def __init__(self, main_hand=None, off_hand=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
    # Свойство предмета - бонус к здоровью
    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        return bonus
    # Свойство предмета - бонус к броне
    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        return bonus
    # Свойство предмета - бонус к атаке
    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        return bonus
    # Переключение состояния(экипировано\не экипировано) предмета
    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot
        # Для слота MAIN_HAND
        if slot == EquipmentSlots.MAIN_HAND:
            # Если предмет находтся экипирован, снимаем его
            if self.main_hand == equippable_entity:
                self.main_hand = None
                # результат - снят
                results.append({'dequipped': equippable_entity})
            else:
                # Если в слот экипировано что-то еще, снимаем экипированый
                # предмет
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})
                # Надеваем выбраный предмет
                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        # Тоже самое для слота OFF_HAND
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
