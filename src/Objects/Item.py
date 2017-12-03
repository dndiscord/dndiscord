from src import Constants
from src.Objects.GenericObject import GenericObject


class Item(GenericObject):
    def __init__(self, itemConfig):
        super().__init__(itemConfig)
        self.effect = itemConfig[Constants.effect]

    def activate(self, user, isCrit):
        return {
            Constants.description: "{} used {} to {}".format(user.name, self.name, self.effect),
            Constants.attack: user.attack + self.attack,
            Constants.effect: self.effect
        }

    def receive(self, change):
        baseResult = super().receive(change)
        if isinstance(baseResult, list):
            # Return the loot
            return baseResult
        #Handle peaceful interactions with characters
        if baseResult == Constants.take:
            return self