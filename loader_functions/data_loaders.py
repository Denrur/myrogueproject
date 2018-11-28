import shelve
import os


# Функция, сохраняющая пераметры текущей игры в файл
def save_game(player, entities, game_map, message_log, game_state):
    with shelve.open('savegame', 'n') as data_file:
        # Сохраняет индекс игрока из списка сущностей
        data_file['player_index'] = entities.index(player)
        # Сохраняет список кущностей
        data_file['entities'] = entities
        # Сохраняет текущую игровую карту
        data_file['game_map'] = game_map
        # Сохраняет текущий игровой лог
        data_file['message_log'] = message_log
        # Сохраняет текущее состояние игры
        data_file['game_state'] = game_state


# Функция, загружающая параметры игры из файла и возвращающая значение этих
# параметров
def load_game():
    if not os.path.isfile('savegame.db'):
        raise FileNotFoundError

    with shelve.open('savegame', 'r') as data_file:
        player_index = data_file['player_index']
        entities = data_file['entities']
        game_map = data_file['game_map']
        message_log = data_file['message_log']
        game_state = data_file['game_state']
    # Сохраняет в переменную Player  сущность с индексом игрока
    player = entities[player_index]

    return player, entities, game_map, message_log, game_state
