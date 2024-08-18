from .item import Item, Slots


class Sword(Item):
    def __init__(self):
        super().__init__(
            "Sword",
            15,
            "increases attack power when equipped",
            Slots.WEAPON,
            20,
            15,
        )

    def effect(self, target):
        target.add_attack_power(self._effect_value)

    def remove_effect(self, target):
        target.add_attack_power(-self._effect_value)
