from src import Constants
from src.Objects.GenericObject import GenericObject


class Character(GenericObject):
    def __init__(self, characterconfig):
        super().__init__(characterconfig)
        self.crit = characterconfig[Constants.crit]
        self.speed = characterconfig[Constants.speed]
        self.mana = characterconfig[Constants.mana]
        self.user = characterconfig[Constants.user]

    def use_item(self, item, target, action):
        # Result contains a payload of data to apply to the target
        result = item.activate(self, True)
        maybe_loot = target.receive(result)
        if maybe_loot is not None:
            self.inventory.extend(maybe_loot)
        return result[Constants.description]

    def use_person(self, person, action):
        return "{} {}-ed {}".format(self.name, action, person.name)
