from src import Constants
from src.Objects.GenericObject import GenericObject


class Character(GenericObject):
    def __init__(self, characterconfig):
        super().__init__(characterconfig)
        self.crit = characterconfig[Constants.crit]
        self.inventory = characterconfig[Constants.inventory]
        self.attack = characterconfig[Constants.attack]
        self.speed = characterconfig[Constants.speed]
        self.mana = characterconfig[Constants.mana]

    def use_item(self, item, target):
        # Result contains a payload of data to apply to the target
        result = item.activate(self, True)
        target.receive(result)
        return result[Constants.description]


