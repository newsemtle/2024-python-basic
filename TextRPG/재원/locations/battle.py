from math import sqrt
from random import randint

from .location import Location


class Battle(Location):
    def __init__(self, name, level):
        super().__init__(name)
        self._level = level
        self._enemies = []

    @property
    def enemies(self):
        return self._enemies

    def init_enemies(self, enemies):
        self._enemies.clear()
        for enemy in enemies:
            enemy = enemy()
            enemy.level_up(self._level - 1)
            self._enemies.append(enemy)

    def roll_dice(self):
        return randint(1, 6)

    def get_index_of_attacker(self, dice):
        max_value = max(dice)
        return dice.index(max_value)

    def get_index_of_defender(self, dice):
        min_value = min(dice)
        return dice.index(min_value)

    def calculate_reward(self):
        exp = sqrt(self._level) * 10
        gold = sqrt(self._level) * 5
        return exp, gold

    def calculate_penalty(self):
        exp = sqrt(self._level) * 3
        gold = sqrt(self._level) * 2
        return exp, gold
