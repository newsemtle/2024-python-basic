from .character import Character


class Warrior(Character):
    def __init__(self):
        super().__init__("Warrior", 150, 50, 20, 15, 1.3)

    def skill(self, enemy_target, ally_target):
        skill_type = "attack"
        enemy_target.take_damage(self._attack_power * self._skill_power)
        self._mana -= self._mana_cost
        return skill_type
