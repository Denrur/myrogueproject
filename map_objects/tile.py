class Tile:
    """
    A tile on a map. It may or may not be blocked,
    and may or may not block sight
    """

    # Определяет свойство тайла блокировать движение и блокировать поле
    # зрения(прозрачность)
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # По умолчанию, если тайл блокирует движение, он непрозрачный
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
        # Определяет, исследован ли тайл( по умолчанию не исследован)
        self.explored = False
