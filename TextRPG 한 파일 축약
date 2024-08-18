import keyboard
import os
import time
import random


class GameState:
    def __init__(self):
        self.game_over = False

class Menu:
    def __init__(self, text, options):
        self.text = text
        self.options = options
        self.current_option = 0

    def print_menu(self):
        os.system('cls')
        print(self.text)

    def print_options(self):
        current_option_key = list(self.options.keys())[self.current_option]
        options_text = ""

        for option in self.options:
            if option == current_option_key:
                options_text = options_text + ">" + self.options[option] + "<\n"
            else:
                options_text = options_text + self.options[option] + "\n"

        print(options_text)
    
    def choice(self):
        while True:
            if keyboard.is_pressed('up'): #위쪽 방향키 입력
                if self.current_option > 0:
                    self.current_option -= 1
                self.print_menu()
                self.print_options()
                time.sleep(0.1)

            elif keyboard.is_pressed('down'): #아래쪽 방향키 입력
                if self.current_option < len(self.options) - 1:
                    self.current_option += 1
                self.print_menu()
                self.print_options()
                time.sleep(0.1)

            elif keyboard.is_pressed('enter'):
                return list(self.options.keys())[self.current_option]

            time.sleep(0.1)

class Characters:
    def __init__(self, job):
        self.name = "플레이어"
        self.job = job
        self.health = 0
        self.mana = 0
        self.attack_power = 0
        self.level = 1
        self.experience = 0
        self.money = 100 # 기본 돈 설정
        self.inventory = []
        self.set_initial_stats()

    def set_initial_stats(self):
        if self.job == "검사":
            self.health = 150
            self.mana = 50
            self.attack_power = 20
        elif self.job == "마법사":
            self.health = 120
            self.mana = 150
            self.attack_power = 25
        elif self.job == "힐러":
            self.health = 120
            self.mana =100
            self.attack_power = 15
        elif self.job == "탱커":
            self.health = 200
            self.mana = 50
            self.attack_power = 10

    def gain_experience(self, exp):
        self.experience += exp
        while self.experience >= 100:
            self.experience -= 100
            self.level_up()

    def lose_experience(self, exp):
        if self.experience <= exp:
            print("f{self.experience}의 경험치를 잃었습니다. 현재 경험치 : 0")
            self.experience = 0
            time.sleep(3)

        else:
            self.experience -= exp
            print(f"{exp}의 경험치를 잃었습니다. 현재 경험치 : {self.experience}")
            time.sleep(3)

    def level_up(self):
        self.level += 1
        self.health += 10
        self.mana += 7
        self.attack_power += 5
        print(f"레벨 업! 현재 레벨 : {self.level}")
        print(f"체력 : {self.health}, 마나 : {self.mana}, 공격력 : {self.attack_power}")
        time.sleep(3)


    def status(self):
        text = (
            f"\n현재 상태:\n"
            f"돈: {self.money}\n"
            f"인벤토리: {', '.join(self.inventory) if self.inventory else '없음'}\n"
            # .join() : 리스트를 구분자를 추가하여 문자열로 만듦.
            f"체력 : {self.health}, 마나 : {self.mana}, 공격력 : {self.attack_power}\n"
        )
        return text

    def __str__(self): ##__str__ : 객체를 출렬할 떄 넘겨주는 형식을 지정해주는 메소드
        return (f"직업 : {self.job}\n"
                f"레벨 : {self.level}\n"
                f"체력 : {self.health}\n"
                f"마나 : {self.mana}\n"
                f"공격력 : {self.attack_power}\n"
                f"경험치 : {self.experience}\n"
                f"돈 : {self.money}\n"
                f"아이템 : {self.inventory}\n") 

#character.buy_item("방어구", 50, {"health" : 20}

    def buy_item(self, item_name, cost, effect):
        if self.money >= cost:
            self.money -= cost
            for key, value in effect.items():
                setattr(self, key, getattr(self, key) + value)
            #먼저 getattr(self, key)로 현재 속성 값을 가져오고, 그 값에 value를 더한 다음
            #setattr(self, key, ...)로 해당 속성에 새로운 값을 설정합니다.
            self.inventory.append(item_name)
            print(f"{item_name}을(를) 구매하였습니다.")
            time.sleep(2)
        else : 
            print("돈이 부족합니다.")
            time.sleep(2)

class Enemy:
    def __init__(self, level):
        self.name = "적"
        self.level = level
        self.health = 50 + (level * 10)
        self.attack_power = 10 + (level * 5)

    def __str__(self):
        return (f"적 레벨 : {self.level}\n"
                f"체력 : {self.health}\n"
                f"공격력 : {self.attack_power}\n")
    

def select_job():
    text = "직업을 선택하세요\n"

    options = {
        "검사" : "검사",
        "마법사" : "마법사",
        "힐러" : "힐러",
        "탱커" : "탱커",
    }

    job_menu = Menu(text, options)
    job_menu.print_menu()
    job_menu.print_options()
    choice = job_menu.choice()

    return choice


def battle(character, enemy):
    os.system('cls')
    print(f"{enemy.name}을 만났습니다! {enemy.name}을 무찌르고 승리하십시오.")
    time.sleep(2)
    health = character.health

    while character.health > 0 and enemy.health > 0:
        os.system('cls')
        print("플레이어의 상태")
        print(character)
        print("적의 상태")
        print(enemy)
        
        print("전투를 시작합니다.. 주사위를 돌려주세요(..enter)")
        keyboard.wait('enter')
        print("주사위를 돌립니다...")
        time.sleep(1)
        player_roll1 = random.randint(1, 6)
        player_roll2 = random.randint(1, 6)
        player_sum = player_roll1 + player_roll2
        enemy_roll1 = random.randint(1, 6)
        enemy_roll2 = random.randint(1, 6)
        enemy_sum = enemy_roll1 + enemy_roll2
        print(f"{character.name} 결과")
        print(f"{player_roll1} + {player_roll2} = {player_roll1 + player_roll2}")
        print(f"{enemy.name}의 결과")
        print(f"{enemy_roll1} + {enemy_roll2} = {enemy_roll1 + enemy_roll2}")
        time.sleep(2)

        if player_sum >= enemy_sum:
            print("플레이어의 공격!")
            enemy.health -= character.attack_power
            print(f"{enemy.name}에게 {character.attack_power}의 피해를 입혔다!")
            print("다음 턴으로..(enter)")
            keyboard.wait('enter')
        else:
            print("적의 공격!")
            character.health -= enemy.attack_power
            print(f"{enemy.attack_power}의 피해를 입었다!")
            print("다음 턴으로..(enter)")
            keyboard.wait('enter')
        
        time.sleep(3)

        if enemy.health <= 0:
            os.system('cls')
            character.health = health
            print(f"{enemy.name}을 물리쳤습니다!")
            exp_gain = max(100 - (character.level * 10), 1)
            print(f"{exp_gain}의 경험치를 얻었습니다!")
            character.gain_experience(exp_gain)

            character.money += 30
            print("돈 30을 획득하였습니다!")

            time.sleep(3)
            return True
        
        if character.health <= 0:
            os.system('cls')
            character.health = health
            print("플레이어가 패배했습니다...")
            character.lose_experience(50)
            time.sleep(3)

            return False
    return False



def initialize_game(game_state):
    text = (
        "안녕하세요\n"
        "게임의 세계에 오신 것을 환영합니다."
    )

    options = {
        "game_start" : "게임 시작",
        "exit" : "게임 종료",
    }

    starting_menu = Menu(text, options)
    starting_menu.print_menu()
    starting_menu.print_options()
    choice = starting_menu.choice()

    return choice

######################
def game_start():
    os.system('cls')
    print("게임이 시작됩니다.")
    time.sleep(1)

    job = select_job()


    character = Characters(job)
    os.system('cls')


    print(f"환영합니다, {character.name}!")
    time.sleep(1)
    print("\n<상태창>")
    print(character)
    print("넘어가려면 엔터를 눌러주세요.")
    keyboard.wait('enter') ## Enter 누를 때까지 무한루프

    while True:
        os.system('cls')
        time.sleep(1)

        text = (
            "현재 위치 : 집\n"
            "\n<상태창>\n"
            f"{character}\n"
            "무엇을 하시겠습니까\n"
        )
        options = {
            1 : "집으로 가기",
            2 : "상점 방문",
            3 : "전장으로 가기",
            4 : "종료"
        }
        map_menu = Menu(text, options)
        map_menu.print_menu()
        map_menu.print_options()
        choice = map_menu.choice()

        if choice == 1:
            print("현재 집입니다.")
            time.sleep(3)
        elif choice == 2:
            visit_shop(character)
        elif choice == 3:
            go_to_battlefield(character)
        elif choice == 4:
            break
            

        
def visit_shop(character):
    os.system('cls')


    while True:
        text = (
        "상점에 오신 것을 환영합니다. 무엇을 구매하시겠습니까?\n"
        f"{character.status()}"
    )
    
        options = {
        "armor" : "방어구 (50G) : 체력 + 20",
        "spellbook" : "마법서 (70G) : 마나 + 50",
        "sword" : "검 (100G) : 공격력 + 15",
        "exit" : "상점 나가기"
    }
        shop_menu = Menu(text, options)
        shop_menu.print_menu()
        shop_menu.print_options()
        choice = shop_menu.choice()

        if choice == "armor":
            character.buy_item("방어구", 50, {"health" : 20})
        elif choice == "spellbook":
            character.buy_item("마법서", 70, {"mana" : 50})
        elif choice == "sword":
            character.buy_item("검", 100, {"attack_power" : 15})
        elif choice == "exit":
            break
        
    print("계속하려면 엔터를 누르세요.")
    keyboard.wait('enter')



def go_to_battlefield(character):
    os.system('cls')
    print("전장으로 이동합니다...")
    time.sleep(2)
    enemy = Enemy(character.level)

    battle_result = battle(character, enemy)

    if battle_result:
        print("전투에서 승리했습니다.")
        print("enter를 누르면 넘어갑니다...")
        keyboard.wait('enter')
    else:
        print("전투에서 패배했습니다. 게임 오버")
        character.health = 0
        print("enter를 누르면 넘어갑니다...")
        keyboard.wait('enter')
    


def main_game():
    gs = GameState()

    while not gs.game_over:
        choice = initialize_game(gs)
        if choice == "game_start":
            game_start()
        elif choice == "exit":
            gs.game_over = True



if __name__ == "__main__" :
    main_game()
