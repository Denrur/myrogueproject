import tcod
import textwrap


class Message:
    # Свойства сообщения - текст и цвет текста(по умолчанию белый)
    def __init__(self, text, color=tcod.white):
        self.text = text
        self.color = color


class MessageLog:
    # Свойства лога сообщений
    # по умолчанию пустой список сообщений, координата левой верхней вершины
    # ширина и высота лога
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height
    # Сообщение добавляется в лог и подгоняется по ширине лога
    def add_message(self, message):
        # Строка сообщения разбивается на подстроки длиной равной ширине лога
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # Если буфер лога заполнен, удаляем первую строку в списке
            #
            if len(self.messages) == self.height:
                del self.messages[0]
            # Добавляем новую строку как объект Message, содержащий строку
            # сообщения и цвет строки
            self.messages.append(Message(line, message.color))
