import copy

from src import Constants


class GenericObject:
    # assign value, health, name, description
    def __init__(self, objectconfig):
        self.name = objectconfig[Constants.name]
        self.description = objectconfig[Constants.description]
        self.value = objectconfig[Constants.value]
        self.health = objectconfig[Constants.health]
        self.attack = objectconfig[Constants.attack]
        self.inventory = []
        if Constants.inventory in objectconfig.keys():
            self.inventory = objectconfig[Constants.inventory]

    def receive(self, change):
        self.health -= change[Constants.attack]
        if change[Constants.effect] is not None:
            self.description += " [{}]".format(change[Constants.effect])
        if self.health <= 0 < change[Constants.attack]:
            self.description += " [{}]".format("destroyed")
            loot = copy.copy(self.inventory)
            self.inventory = []
            return loot
        return change[Constants.action]