from .item import Item, Slots


class Armor(Item):
    def __init__(self):
        super().__init__(
            "Armor",
            20,
            "increases max health when equipped",
            Slots.ARMOR,
            30,
            20,
        )

    def effect(self, target):
        target.add_health_max(self._effect_value)

    def remove_effect(self, target):
        target.add_health_max(-self._effect_value)
