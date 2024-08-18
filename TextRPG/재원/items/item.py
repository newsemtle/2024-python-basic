from abc import ABC, abstractmethod
from enum import Enum


class Slots(Enum):
    ARMOR = 1
    WEAPON = 2


class Item(ABC):
    def __init__(self, name, effect_value, description, slot, buy_price, sell_price):
        self._name = name
        self._effect_value = effect_value
        self._description = description
        self._slot = slot
        self._buy_price = buy_price
        self._sell_price = sell_price

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def slot(self):
        return self._slot

    def get_price(self, is_buying=True):
        if is_buying:
            return self._buy_price
        else:
            return self._sell_price

    @abstractmethod
    def effect(self, target):
        pass

    @abstractmethod
    def remove_effect(self, target):
        pass
