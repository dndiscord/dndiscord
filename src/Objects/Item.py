from src import Constants
from src.Objects.GenericObject import GenericObject


class Item(GenericObject):
    def __init__(self, itemConfig):
        super().__init__(itemConfig)
        self.effect = itemConfig[Constants.effect]

    def activate(self, user, isCrit):
        return {
            Constants.description: "{} used {} to {}".format(user.name, self.name, self.effect),
            Constants.health: self.health,
            Constants.effect: self.effect
        }
