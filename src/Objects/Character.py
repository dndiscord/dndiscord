from src import Constants
from src.Objects.GenericObject import GenericObject


class Character(GenericObject):
    def __init__(self, characterconfig):
        self.crit = characterconfig[Constants.crit]
        self.inventory = characterconfig[Constants.inventory]

    def use_item(self, item_name):
        # If the requested item isnt in the inventory
        item = next(iter([item for item in self.inventory if item.name == item_name] or []), None)
        if item is None:
            self
        else:
            item.activate(self, True, "A fireball is thrown")


