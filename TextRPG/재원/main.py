from game import GameManager, WorldMap
from ui import CLI


def main():
    game_manager = GameManager()
    game_map = WorldMap()
    cli = CLI(game_manager, game_map)
    cli.start_menu()
    while True:
        cli.main_menu()
        while True:
            back_to_main_menu = cli.world_map()
            if back_to_main_menu:
                break


if __name__ == "__main__":
    main()
