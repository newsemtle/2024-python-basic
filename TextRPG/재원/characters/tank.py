from .character import Character


class Tank(Character):
    def __init__(self):
        super().__init__("Tank", 200, 50, 10, 20, 1.2)

    def skill(self, enemy_target, ally_target):
        skill_type = "attack"
        enemy_target.take_damage(self._attack_power * self._skill_power)
        self._mana -= self._mana_cost
        return skill_type
