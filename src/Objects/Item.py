from src import Constants
from src.Objects.GenericObject import GenericObject


class Item(GenericObject):
    def __init__(self,itemConfig):
        super().__init__(itemConfig)
        self.effect = itemConfig[Constants.effect]

    def activate(self,user,isCrit):
        return {Constants.effect: "{} used {} to do {}".format(user.name,self.name,self.effect)}
