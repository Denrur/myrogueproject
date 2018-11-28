class Item:
    # Класс определяет наличие у предмета функции использования,
    # функции выбора цели, сообщения при выборе цели, и дополнительных функций
    def __init__(self, use_function=None, targeting=False,
                 targeting_message=None, **kwargs):
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.function_kwargs = kwargs
