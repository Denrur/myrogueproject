class Rect:
    # Параметры класса - координаты левой верхней вершины прямоугольника
    # ширины и высоты
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    # Расчет центра прямоугольника
    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return (center_x, center_y)

    # Определение пересечения прямоугольника с другим прямоугольником
    def intersect(self, other):
        # Возвращает True если есть пересечение
        return (self.x1 <= other.x2 and
                self.x2 >= other.x1 and
                self.y1 <= other.y2 and
                self.y2 >= other.y1)
