from enum import Enum

import locations
from locations.location import Location


class MapLocations(Enum):
    HOME = 1
    SHOP = 2
    BATTLE_1 = 11
    BATTLE_2 = 12
    BATTLE_3 = 13


class WorldMap:
    def __init__(self):
        self._location_infos = self._init_location_infos()
        self._current_location = None

    def _init_location_infos(self):
        home = locations.Home("Home")
        shop = locations.Shop("Shop")
        battle_1 = locations.Battle("Battle 1", 1)
        battle_2 = locations.Battle("Battle 2", 6)
        battle_3 = locations.Battle("Battle 3", 11)
        home.add_connections_with(shop, battle_1, battle_2, battle_3)
        battle_1.add_links_to(battle_2)
        battle_2.add_links_to(battle_3)

        return {
            MapLocations.HOME: home,
            MapLocations.SHOP: shop,
            MapLocations.BATTLE_1: battle_1,
            MapLocations.BATTLE_2: battle_2,
            MapLocations.BATTLE_3: battle_3,
        }

    @property
    def location_infos(self):
        return self._location_infos

    @property
    def current_location(self):
        return self._current_location

    def navigate(self, destination: MapLocations):
        if destination in MapLocations:
            self._current_location = destination
            return destination
        else:
            raise ValueError("Invalid destination")

    def get_location_key(self, location: Location):
        for key, value in self.location_infos.items():
            if value == location:
                return key
