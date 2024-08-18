from random import randint

import data
from characters import CHARACTERS
from game import MapLocations
from utils import clear_screen, get_key_release


class CLI:
    def __init__(self, game_manager, game_map):
        self.gm = game_manager
        self.map = game_map

    @staticmethod
    def start_menu():
        clear_screen()
        print("=== TextRPG ===")
        print("Press ENTER to start...")
        while True:
            key = get_key_release()
            if key == "enter":
                break
            else:
                continue

    def main_menu(self):
        clear_screen()
        print("=== TextRPG ===")
        options = [
            "Continue",
            "New Game",
            "Quit",
        ]
        self._display_options(options)
        print("===============")

        choice = self._get_valid_choice(options)
        handlers = [
            self._continue_game,
            self._new_game,
            self._quit_game,
        ]
        handlers[choice]()

    def select_characters(self):
        clear_screen()
        print("Choose two characters:")
        self._display_options([character().name for character in CHARACTERS])
        print("===============")

        unselected_characters = CHARACTERS[:]  # shallow copy
        while len(unselected_characters) > 2:
            choice = self._get_valid_choice(CHARACTERS)
            character = CHARACTERS[choice]
            if character in unselected_characters:
                unselected_characters.remove(character)
                self.gm.add_ally(character())
                print(f"\033[1;33m{character.__name__}\033[0m")
            else:
                print("Character already selected.")
        for character in unselected_characters:
            self.gm.add_enemy(character)

    def world_map(self):
        location_infos = self.map.location_infos
        current_location = self.map.current_location
        location_names = self._format_location_names(location_infos, current_location)
        clear_screen()
        print("=== World Map ===")
        self._display_map(location_names)
        print("===============")

        print("Enter the number of the location to navigate and press ENTER")
        print("Enter '0' to go back to Main Menu")
        choice = self._get_valid_location_choice(location_infos, current_location)
        if choice == 0:
            return True
        else:
            new_location = self.map.navigate(MapLocations(choice))
            handlers = {
                MapLocations.HOME: self.home_menu,
                MapLocations.SHOP: self.shop_menu,
                MapLocations.BATTLE_1: self.battle_menu,
                MapLocations.BATTLE_2: self.battle_menu,
                MapLocations.BATTLE_3: self.battle_menu,
            }
            handler = handlers[new_location]
            if handler:
                handler(location_infos[new_location])
            return False

    def home_menu(self, _):
        while True:
            clear_screen()
            print("=== Home ===")
            options = [
                "Sleep",
                "Inventory",
                "Character Status",
                "Exit",
                "Save Game",
                "Quit Game",
            ]
            self._display_options(options)
            print("===============")

            choice = self._get_valid_choice(options)
            if choice == 3:
                return
            else:
                handlers = [
                    self._sleep,
                    self.inventory,
                    self.character_status,
                    None,
                    self._save_game,
                    self._quit_game,
                ]
                handlers[choice]()

    def inventory(self):
        while True:
            clear_screen()
            print("=== Inventory ===")
            inv, inv_size = self.gm.get_inventory_data()
            self._display_inventory(inv, inv_size)
            print("Select an item to equip")
            print("Press 'q' to go back")
            print("===============")
            choice = self._get_valid_choice_with_escaping(inv)
            if choice is None:
                return
            selected_item = inv[choice]
            print(f"Selected item: {selected_item.name}")

            print("Select a character to equip the item")
            print("press 'q' to cancel")
            self._display_options(self.gm.allies)
            choice = self._get_valid_choice_with_escaping(self.gm.allies)
            if choice is None:
                continue
            selected_character = self.gm.allies[choice]
            selected_character.equip(selected_item)
            self.gm.remove_from_inventory(selected_item)
            print("Item equipped successfully.")
            input("Press ENTER to continue")

    def character_status(self):
        clear_screen()
        print("=== Character Status ===")
        for character in self.gm.allies:
            self._display_character_status(character)
        print("Press 'u' to unequip items from character")
        print("Press 'q' to go back")
        while True:
            key = get_key_release()
            if key == "u":
                self.unequip_menu()
            elif key == "q":
                break
            else:
                continue

    def unequip_menu(self):
        while True:
            clear_screen()
            print("=== Unequip Menu ===")
            for i, character in enumerate(self.gm.allies, start=1):
                print(f"[{i}] \033[1;33m{character.name}\033[0m")
                self._display_equipments(character)
                print("===============")
            print("Select a character to unequip an item")
            print("Press 'q' to go back")
            choice = self._get_valid_choice_with_escaping(self.gm.allies)
            if choice is None:
                return
            selected_character = self.gm.allies[choice]
            clear_screen()
            print(f"\033[1;33m{character.name}\033[0m")
            self._display_equipments(selected_character, enumeration=True)
            print("===============")
            print("Select an item to unequip")
            print("Press 'q' to cancel")
            equipment = selected_character.equipment
            choice = self._get_valid_choice_with_escaping(equipment)
            if choice is None:
                continue
            selected_item = list(equipment.values())[choice]
            if selected_item is not None:
                selected_character.unequip(selected_item)
                self.gm.add_to_inventory(selected_item)
            else:
                print("No item equipped.")

    def shop_menu(self, shop):
        while True:
            clear_screen()
            print("=== Shop ===")
            options = [
                "Buy",
                "Sell",
                "Exit",
            ]
            self._display_options(options)
            print("===============")
            choice = self._get_valid_choice(options)
            if choice == 2:
                return
            else:
                handlers = [
                    self.shop_buy_menu,
                    self.shop_sell_menu,
                    None,
                ]
                handlers[choice](shop)

    def shop_buy_menu(self, shop):
        while True:
            shop_items = shop.get_shop_data()
            clear_screen()
            print("=== Buy ===")
            self._display_shop(shop_items)
            print("Select an item to buy")
            print("Press 'q' to go back")
            confirmed = self._get_valid_choice_with_escaping(shop_items)
            if confirmed is None:
                return
            selected_item = shop_items[confirmed].item
            print(f"Do you want to buy {selected_item.name}?")
            print("Press 'y' to confirm or 'n' to cancel")
            confirmed = self._get_confirmation()
            if not confirmed:
                continue
            inv, inv_size = self.gm.get_inventory_data()
            if len(inv) >= inv_size:
                print("Inventory is full.")
                input("Press ENTER to continue")
                continue
            elif self.gm.gold < selected_item.get_price():
                print("Not enough gold.")
                input("Press ENTER to continue")
                continue
            result = shop.remove_item(selected_item)
            if result == -1:
                print("Item not found in the shop.")
                input("Press ENTER to continue")
                continue
            self.gm.add_to_inventory(selected_item)
            self.gm.add_gold(-selected_item.get_price())
            print(f"{selected_item.name} purchased successfully.")
            input("Press ENTER to continue")

    def shop_sell_menu(self, shop):
        while True:
            clear_screen()
            print("=== Sell ===")
            inv, inv_size = self.gm.get_inventory_data()
            self._display_inventory(inv, inv_size)
            print("Select an item to sell")
            print("Press 'q' to go back")
            choice = self._get_valid_choice_with_escaping(inv)
            if choice is None:
                return
            selected_item = inv[choice]
            print(f"Do you want to sell {selected_item.name}?")
            print("Press 'y' to confirm or 'n' to cancel")
            confirmed = self._get_confirmation()
            if not confirmed:
                continue
            self.gm.remove_from_inventory(selected_item)
            shop.add_item(selected_item)
            self.gm.add_gold(selected_item.get_price(False))
            print(f"{selected_item.name} sold successfully.")
            input("Press ENTER to continue")

    def battle_menu(self, battle):
        battle.init_enemies(self.gm.enemies)
        clear_screen()
        print("=== Encounter ===")
        self._display_characters_info(battle.enemies)
        print("===============")
        print("Do you want to fight?")
        print("Press 'y' to confirm or 'n' to run away")
        confirmed = self._get_confirmation()
        if confirmed:
            self.start_battle(battle)
        else:
            print("You ran away from the battle.")
            input("Press ENTER to return to World Map")

    def start_battle(self, battle):
        max_round = 15
        for battle_round in range(1, max_round + 1):
            clear_screen()
            print("=== Battle ===")
            print("Allies:")
            self._display_characters_info(self.gm.allies)
            print("Enemies:")
            self._display_characters_info(battle.enemies)
            print("===============")
            print(f"Round {battle_round}/{max_round}")
            print("Rolling dice to determine attack and defense for this round.")
            input("Press ENTER to roll the dice")
            dice = []
            for _ in range(4):
                dice.append(battle.roll_dice())
            ally_dice = dice[:2]
            enemy_dice = dice[2:]
            for i, roll in enumerate(ally_dice):
                print(f"{self.gm.allies[i].name} rolled {roll}")
            print(f"Ally: {sum(ally_dice)}")
            for i, roll in enumerate(enemy_dice):
                print(f"{battle.enemies[i].name} rolled {roll}")
            print(f"Enemy: {sum(enemy_dice)}")

            team_dice = [sum(ally_dice), sum(enemy_dice)]
            team_index = battle.get_index_of_attacker(team_dice)

            ally_attacker = self.gm.allies[battle.get_index_of_attacker(ally_dice)]
            ally_defender = self.gm.allies[battle.get_index_of_defender(ally_dice)]
            if ally_attacker.is_faint():
                ally_attacker = ally_defender
            elif ally_defender.is_faint():
                ally_defender = ally_attacker
            enemy_attacker = battle.enemies[battle.get_index_of_attacker(enemy_dice)]
            enemy_defender = battle.enemies[battle.get_index_of_defender(enemy_dice)]
            if enemy_attacker.is_faint():
                enemy_attacker = enemy_defender
            elif enemy_defender.is_faint():
                enemy_defender = enemy_attacker

            if team_index == 0:
                print("Allies attack first.")
                input("Press ENTER to continue")
                print("Ally's turn")
                self._ally_attack(ally_attacker, enemy_defender, ally_defender)
                if self._is_battle_over(self.gm.allies, battle.enemies):
                    break
                print("===============")
                print("Enemy's turn")
                self._enemy_attack(enemy_attacker, ally_defender, enemy_defender)
                if self._is_battle_over(self.gm.allies, battle.enemies):
                    break
                print("===============")
            else:
                print("Enemies attack first.")
                input("Press ENTER to continue")
                print("Enemy's turn")
                self._enemy_attack(enemy_attacker, ally_defender, enemy_defender)
                if self._is_battle_over(self.gm.allies, battle.enemies):
                    break
                print("===============")
                print("Ally's turn")
                self._ally_attack(ally_attacker, enemy_defender, ally_defender)
                if self._is_battle_over(self.gm.allies, battle.enemies):
                    break
                print("===============")
        if battle_round >= max_round:
            print("Battle ended in a draw.")
        else:
            print("Battle ended")
            if self._did_ally_win(self.gm.allies):
                print("Won the battle!")
                exp, gold = battle.caculate_reward()
                for ally in self.gm.allies:
                    ally.add_exp(exp)
                    self.gm.add_gold(gold)
                print(f"Reward: Gained {gold}G and {exp}exp for each characters")
            else:
                print("Lost the battle.")
                exp, gold = battle.caculate_penalty()
                for ally in self.gm.allies:
                    ally.add_exp(-exp)
                    self.gm.add_gold(-gold)
                print(f"Penalty: Lost {gold}G and {exp}exp for each characters")
        input("Press ENTER to return to World Map")

    def _get_confirmation(self):
        while True:
            key = get_key_release()
            if key == "y":
                return True
            elif key == "n":
                return False
            else:
                continue

    def _get_valid_choice(self, options):
        while True:
            key = get_key_release()
            if key.isdigit() and 1 <= int(key) <= len(options):
                return int(key) - 1
            else:
                continue

    def _get_valid_choice_with_escaping(self, options):
        while True:
            key = get_key_release()
            if key == "q":
                return None
            elif key.isdigit() and 1 <= int(key) <= len(options):
                return int(key) - 1
            else:
                continue

    def _get_valid_location_choice(self, location_infos, current_location):
        while True:
            value = input()
            number = int(value) if value.isdigit() else -1
            valid_list = []
            valid_list.append(0)
            valid_list.append(current_location.value)
            valid_list += [
                self.map.get_location_key(loc).value
                for loc in location_infos[current_location].links
            ]
            if number in valid_list:
                return number
            else:
                print("You can't go there")
                continue

    def _format_location_names(self, location_infos, current_location):
        locations = {}
        for enum, info in location_infos.items():
            if enum == current_location:
                locations[enum] = f"{enum.value}. \033[1;33m{info.name}\033[0m"
            elif info in self.map.location_infos[current_location].links:
                locations[enum] = f"{enum.value}. \033[1;32m{info.name}\033[0m"
            else:
                locations[enum] = f"{enum.value}. {info.name}"
        return locations

    def _display_map(self, location_names):
        home = location_names[MapLocations.HOME]
        shop = location_names[MapLocations.SHOP]
        battle_1 = location_names[MapLocations.BATTLE_1]
        battle_2 = location_names[MapLocations.BATTLE_2]
        battle_3 = location_names[MapLocations.BATTLE_3]
        print(f"{shop} ── {home} ── {battle_1}")
        print(f"                │            ↓    ")
        print(f"                ├──── {battle_2}")
        print(f"                │            ↓    ")
        print(f"                └──── {battle_3}")

    def _display_options(self, options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def _display_shop(self, shop_items):
        for i, shop_item in enumerate(shop_items, start=1):
            item = shop_item.item
            print(f"{i}. {item.name:<12} | {item.get_price():>3}G | x{shop_item.amount}")
            print(f"   : {item.description}")

    def _display_character_status(self, character):
        print(f"\033[1;33m{character.name}\033[0m")
        print(f"Level: {character.level}")
        exp, max_exp = character.get_exp()
        print(f"Exp: {exp}/{max_exp}")
        health, max_health = character.get_health()
        print(f"Health: {health}/{max_health}")
        mana, max_mana = character.get_mana()
        print(f"Mana: {mana}/{max_mana}")
        attack_power, skill_power, mana_cost = character.get_attack_info()
        print(f"Attack: {attack_power}")
        print(f"Skill Power: {skill_power} | Skill Cost: {mana_cost}")
        print("-- Equipments --")
        self._display_equipments(character)
        print("===============")

    def _display_equipments(self, character, enumeration=False):
        if enumeration is True:
            for i, (slot, item) in enumerate(character.equipment.items(), start=1):
                print(f"{i}. {slot.name}: {item.name if item is not None else 'Empty'}")
        else:
            for slot, item in character.equipment.items():
                print(f"{slot.name}: {item.name if item is not None else 'Empty'}")

    def _display_inventory(self, inv, inv_size):
        for i in range(inv_size):
            if i > len(inv) - 1:
                print(f"{i+1}. _________")
            else:
                print(f"{i+1}. {inv[i]}")

    def _display_characters_info(self, characters):
        for i, ally in enumerate(characters, start=1):
            health, max_health = ally.get_health()
            mana, max_mana = ally.get_mana()
            print(
                f"{i}. \033[33m{ally.name:<8}\033[0m | \033[41mHealth: {health}/{max_health}\033[0m | \033[44mMana: {mana}/{max_mana}\033[0m"
            )

    def _continue_game(self):
        if data.has_save_file():
            save_data = data.load_data()
            self.gm.load_game(save_data)
            self.map.navigate(save_data.current_location)
        else:
            print("No save file found.")
            self._new_game()

    def _new_game(self):
        self.select_characters()
        self.map.navigate(MapLocations.HOME)

    def _quit_game(self):
        clear_screen()
        print("Goodbye!")
        exit()

    def _sleep(self):
        for character in self.gm.allies:
            character.recover_health(1000)
            character.recover_mana(1000)
        print("All characters fully recovered their health and mana while sleeping")
        input("Press ENTER to continue")

    def _save_game(self):
        print("Currently in development...")
        if False:
            data.save(self.gm, self.map.current_location)
            print("Game saved successfully")
        input("Press ENTER to continue")

    def _ally_attack(self, attacker, enemy_target, ally_target):
        print(f"{attacker.name} acts this turn. Targets can be")
        print(f"Ally: {ally_target.name}, Enemy: {enemy_target.name}")
        print("Choose your action")
        attack_power, skill_power, mana_cost = attacker.get_attack_info()
        options = [
            f"Attack - power: {attack_power}",
            f"Skill - power: {skill_power * attack_power}, mana cost: {mana_cost}",
        ]
        self._display_options(options)
        choice = self._get_valid_choice(options)
        if mana_cost > attacker.get_mana()[0]:
            print("Not enough mana.")
            choice = 0
        if choice == 0:
            attacker.attack(enemy_target)
            damage = attack_power
            print(f"{attacker.name} used normal attack.")
            print(f"{attacker.name} dealt {damage} damage to {enemy_target.name}")
            input("Press ENTER to continue")
        elif choice == 1:
            skill_type = attacker.skill(enemy_target, ally_target)
            damage = attack_power * skill_power
            print(f"{attacker.name} used skill.")
            if skill_type == "attack":
                print(f"{attacker.name} dealt {damage} damage to {enemy_target.name}")
            elif skill_type == "heal":
                print(f"{attacker.name} healed {damage} HP for {ally_target.name}")
            input("Press ENTER to continue")

    def _enemy_attack(self, attacker, ally_target, enemy_target):
        print(f"{attacker.name} acts this turn. Targets can be")
        print(f"Ally: {ally_target.name}, Enemy: {enemy_target.name}")
        input("Press ENTER to continue")
        attack_power, skill_power, mana_cost = attacker.get_attack_info()
        choice = randint(0, 1)
        if mana_cost > attacker.get_mana()[0]:
            choice = 0
        if choice == 0:
            attacker.attack(ally_target)
            damage = attack_power
            print(f"{attacker.name} used normal attack.")
            print(f"{attacker.name} dealt {damage} damage to {ally_target.name}")
            input("Press ENTER to continue")
        elif choice == 1:
            skill_type = attacker.skill(ally_target, enemy_target)
            damage = attack_power * skill_power
            print(f"{attacker.name} used skill.")
            if skill_type == "attack":
                print(f"{attacker.name} dealt {damage} damage to {ally_target.name}")
            elif skill_type == "heal":
                print(f"{attacker.name} healed {damage} HP for {enemy_target.name}")
            input("Press ENTER to continue")

    def _is_battle_over(self, allies, enemies):
        is_over = self._did_ally_win(allies)
        is_over = self._did_enemy_win(enemies)
        return is_over

    def _did_ally_win(self, allies):
        for ally in allies:
            if not ally.is_faint():
                return False
        return True

    def _did_enemy_win(self, enemies):
        for enemy in enemies:
            if not enemy.is_faint():
                return False
        return True
