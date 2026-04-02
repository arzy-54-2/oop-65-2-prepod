class Hero:

    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты класса
        self.name = name
        self.hp = hp
        self.lvl = lvl

    # Метод класса
    def action(self):
        return f"{self.name} hero base action!!"


# Объект|Экземпляр на основе класса
kirito = Hero("Kirito", 1000, 100)
asuna = Hero("Asuna", 10000, 1000)

