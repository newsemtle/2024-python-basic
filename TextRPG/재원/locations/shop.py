from dataclasses import dataclass

import items
from items.item import Item

from .location import Location


class Shop(Location):
    def __init__(self, name):
        super().__init__(name)
        self.goods = self._init_goods()

    def _init_goods(self):
        armor = ShopItem(items.Armor(), 2)
        sword = ShopItem(items.Sword(), 2)
        spellbook = ShopItem(items.Spellbook(), 2)
        return [armor, sword, spellbook]

    def get_shop_data(self):
        return self.goods

    def add_item(self, item, amount=1):
        index = self._find_item_index(item)
        if index != -1:
            self.goods[index].amount += amount
        else:
            self.goods += ShopItem(item, amount)

    def remove_item(self, item, amount=1):
        index = self._find_item_index(item)
        if index != -1:
            if self.goods[index].amount > amount:
                self.goods[index].amount -= amount
            elif self.goods[index].amount == amount:
                del self.goods[index]
        return -1

    def _find_item_index(self, item):
        for i, shop_item in enumerate(self.goods):
            if shop_item.item == item:
                return i
        return -1


@dataclass
class ShopItem:
    item: Item
    amount: int = 1
