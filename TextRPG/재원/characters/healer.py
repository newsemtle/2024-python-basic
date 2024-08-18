from .character import Character


class Healer(Character):
    def __init__(self):
        super().__init__("Healer", 120, 100, 15, 20, 1)

    def skill(self, enemy_target, ally_target):
        skill_type = "heal"
        ally_target.recover_health(self._skill_power * self._attack_power)
        self._mana -= self._mana_cost
        return skill_type
