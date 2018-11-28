import tcod


# Создаем шаблон меню в который передаем параметры
# консоль, где рендерится меню, заголовок, опции, высоту и длину экрана
def menu(con, header, options, width, screen_width, screen_height):
    # Ограничиваем количество опций, отображаемых в меню
    if len(options) > 26:
                raise ValueError('Cant have a menu with more than 26 options.')

    # Расчитываем высоту заголовка(после автосворачивания) и линий для каждой
    # опции меню

    header_height = tcod.console_get_height_rect(con, 0, 0, width,
                                                 screen_height, header)
    height = len(options) + header_height

    # Создаем консоль, в которой будет отображаться окно меню
    window = tcod.console_new(width, height)

    # Печатаем заголовой с автопереносом и выравниванием по левой стороне окна
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_print_rect_ex(window, 0, 0, width, height,
                               tcod.BKGND_NONE, tcod.LEFT, header)

    # Печатаем все опции, присваивая им буквы по алфавиту
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        tcod.console_print_ex(window, 0, y, tcod.BKGND_NONE, tcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    tcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

# Меню инвентаря принимает параметры
# консоль, заголовок, объект игрока, ширина окна инветаря, ширина и длина
# экрана
def inventory_menu(con, header, player, inventory_width,
                   screen_width, screen_height):
    # Показывает игроку меню инвентаря с предметами в нем в качестве опций
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hend)'.format(item.name))
            else:
                options.append(item.name)

    menu(con, header, options, inventory_width, screen_width, screen_height)

# Главное меню с фоновой картинкой
def main_menu(con, background_image, screen_width, screen_height):
    tcod.image_blit_2x(background_image, 0, 0, 0)

    tcod.console_set_default_foreground(0, tcod.light_yellow)
    tcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2)-4,
                          tcod.BKGND_NONE, tcod.CENTER, 'TOMBS OF THE MUMMY')
    tcod.console_print_ex(con, int(screen_width / 2), int(screen_height - 2),
                          tcod.BKGND_NONE, tcod.CENTER,
                          'By Denrur')

    menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24,
         screen_width, screen_height)

# Меню повышения статов при левелапе
def level_up_menu(con, header, player, menu_width,
                  screen_width, screen_height):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attac, from{0})'.format(player.fighter.power),
               'Agility (+1 defense, from {0})'.format(player.fighter.defense)]

    menu(con, header, options, menu_width, screen_width, screen_height)

# Меню с параметрами персонажа
def character_screen(player, character_screen_width, character_screen_height,
                     screen_width, screen_height):
    window = tcod.console_new(character_screen_width, character_screen_height)

    tcod.console_set_default_foreground(window, tcod.white)

    tcod.console_print_rect_ex(window, 0, 1, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Character Information")
    tcod.console_print_rect_ex(window, 0, 2, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Level: {0}".format(player.level.current_level))
    tcod.console_print_rect_ex(window, 0, 3, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Exp: {0}".format(player.level.current_xp))
    tcod.console_print_rect_ex(window, 0, 4, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Exp to lvl: {0}".format(
                                   player.level.experience_to_next_level))
    tcod.console_print_rect_ex(window, 0, 6, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Max HP: {0}".format(player.fighter.max_hp))
    tcod.console_print_rect_ex(window, 0, 7, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Attack: {0}".format(player.fighter.power))
    tcod.console_print_rect_ex(window, 0, 8, character_screen_width,
                               character_screen_height, tcod.BKGND_NONE,
                               tcod.LEFT,
                               "Defense: {0}".format(player.fighter.defense))

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    tcod.console_blit(window, 0, 0,
                      character_screen_width, character_screen_height,
                      0, x, y, 1.0, 0.7)

# пустое меню без опций
def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)
