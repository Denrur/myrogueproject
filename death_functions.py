import tcod
from game_messages import Message
from game_states import GameStates
from render_functions import RenderOrder

# Функция смерти игрока
def kill_player(player):
    # меняем тайл и цвет тайла игрока
    player.char = '%'
    player.color = tcod.dark_red
    # Возвращаем сообщение о смерти, меняем состояние игры на PLAYER_DEAD
    return Message('You dead!', tcod.red), GameStates.PLAYER_DEAD

# Функция убийства монстра
def kill_monster(monster):
    # Сообщение о смерти
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()),
                            tcod.orange)
    # меняем тайл и цвет тайла монстра
    monster.char = '%'
    monster.color = tcod.dark_red
    # Объект больше не блокирует предвижжение
    monster.blocks = False
    # Убераем компоненты fighter и ai
    monster.fighter = None
    monster.ai = None
    # Меняем имя монстра
    monster.name = 'remains of ' + monster.name
    # Меняем порядок рендера тайла
    monster.render_order = RenderOrder.CORPSE
    # Возвращаем сообщение о смерти
    return death_message
