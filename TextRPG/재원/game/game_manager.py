class GameManager:
    def __init__(self):
        self._gold = 0
        self._inventory = []
        self._inventory_size = 5
        self._allies = []
        self._enemies = []

    @property
    def gold(self):
        return self._gold

    def add_gold(self, amount):
        self._gold += amount
        if self._gold < 0:
            self._gold = 0

    @property
    def allies(self):
        return self._allies

    def add_ally(self, character):
        self._allies.append(character)

    @property
    def enemies(self):
        return self._enemies

    def add_enemy(self, character):
        self._enemies.append(character)

    def clear_characters(self):
        self._allies.clear()
        self._enemies.clear()

    def get_inventory_data(self):
        return (self._inventory, self._inventory_size)

    def add_to_inventory(self, item):
        if len(self._inventory) < self._inventory_size:
            self._inventory.append(item)
            return True
        else:
            return False

    def remove_from_inventory(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
            return True
        else:
            return False
