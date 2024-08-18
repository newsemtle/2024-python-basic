from .item import Item, Slots


class Spellbook(Item):
    def __init__(self):
        super().__init__(
            "Spellbook",
            50,
            "increases max mana when equipped",
            Slots.WEAPON,
            25,
            18,
        )

    def effect(self, target):
        target.add_mana_max(self._effect_value)

    def remove_effect(self, target):
        target.add_mana_max(-self._effect_value)
