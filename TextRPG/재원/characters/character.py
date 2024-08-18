from abc import ABC, abstractmethod

from items.item import Slots


class Character(ABC):
    def __init__(self, name, health, mana, ap, mana_cost, skill_power):
        self._name = name
        self._health = health
        self._health_max = health
        self._mana = mana
        self._mana_max = mana
        self._attack_power = ap
        self._mana_cost = mana_cost
        self._skill_power = skill_power
        self._level = 1
        self._exp = 0
        self._exp_max = 10
        self._equipment = {Slots.WEAPON: None, Slots.ARMOR: None}

    @property
    def name(self):
        return self._name

    def get_health(self):
        return (self._health, self._health_max)

    def is_faint(self):
        return self._health <= 0

    def recover_health(self, amount):
        self._health += amount
        if self._health > self._health_max:
            self._health = self._health_max

    def take_damage(self, amount):
        self._health -= amount
        if self._health < 0:
            self._health = 0

    def add_health_max(self, amount):
        self._health_max += amount

    def get_mana(self):
        return (self._mana, self._mana_max)

    def recover_mana(self, amount):
        self._mana += amount
        if self._mana > self._mana_max:
            self._mana = self._mana_max

    def add_mana_max(self, amount):
        self._mana_max += amount

    def get_attack_info(self):
        return self._attack_power, self._skill_power, self._mana_cost

    def add_attack_power(self, amount):
        self._attack_power += amount

    def attack(self, target):
        target.take_damage(self._attack_power)

    @abstractmethod
    def skill(self, enemy, ally):
        pass

    @property
    def level(self):
        return self._level

    def get_exp(self):
        return (self._exp, self._exp_max)

    def add_exp(self, amount):
        self._exp += amount
        if self._exp < 0:
            self._exp = 0
        while self._exp < self._exp_max:
            self._exp -= self._exp_max
            self.level_up()

    def level_up(self, amount=1):
        self._level += amount * 1
        self._exp_max += amount * 5

        self._health_max += amount * 5
        self._mana_max += amount * 3
        self._attack_power += amount * 2

        self._health = self._health_max
        self._mana = self._mana_max

    @property
    def equipment(self):
        return self._equipment

    def equip(self, item):
        if self._equipment[item.slot] is None:
            self._equipment[item.slot] = item
            item.effect(self)
        elif self._equipment[item.slot] != item:
            self._equipment[item.slot].remove_effect(self)
            self._equipment[item.slot] = item
            item.effect(self)

    def unequip(self, slot):
        self._equipment[slot].remove_effect(self)
        item = self._equipment[slot]
        self._equipment[slot] = None
        return item
