from .healer import Healer
from .mage import Mage
from .tank import Tank
from .warrior import Warrior

__all__ = ["Healer", "Mage", "Tank", "Warrior"]

CHARACTERS = [Warrior, Mage, Healer, Tank]
