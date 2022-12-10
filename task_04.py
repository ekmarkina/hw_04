"""
Создать игровой инвентарь.
Должна быть возможность добавлять в него предметы и удалять предметы из него.
Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес.
Вывод предметов должен быть с названием предмета и его весом.
"""


class Inventory:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        print(f"Создан инвентарь с максимальным весом {self.max_weight} кг.")

    def add_item(self, item):
        if self.get_total_weight() + item.weight <= self.max_weight:
            print(f"Добавлен предмет {item}")
            self.items.append(item)
        else:
            print(f"Инвентарь переполнен! Невозможно добавить предмет {item.name} весом {item.weight} кг.")

    def remove_item(self, item):
        print(f"Удален предмет {item}")
        self.items.remove(item)

    def get_total_weight(self):
        return sum([item.weight for item in self.items])

    def __str__(self):
        return f"Инвентарь ({self.get_total_weight()} кг): {', '.join([str(item) for item in self.items])}"


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} кг)"


def main():
    # Создаем предметы
    sword = Item("Меч", 5)
    shield = Item("Щит", 3)
    potion = Item("Зелье", 1)
    bow = Item("Лук", 2)
    arrow = Item("Стрела", 1)
    # Создаем инвентарь
    inventory = Inventory(10)

    # Добавляем предметы в инвентарь
    inventory.add_item(sword)
    inventory.add_item(shield)
    inventory.add_item(potion)
    print(inventory)

    # Удаляем предмет из инвентаря
    inventory.remove_item(sword)
    print(inventory)

    # Пытаемся добавить предмет, который не влезет в инвентарь
    inventory.add_item(sword)
    inventory.add_item(bow)
    inventory.add_item(arrow)
    print(inventory)


if __name__ == '__main__':
    main()
