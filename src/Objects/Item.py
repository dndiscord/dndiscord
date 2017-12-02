from src import Constants
from src.Objects.GenericObject import GenericObject


class Item(GenericObject):
    def __init__(self,itemConfig):
        self.effect = itemConfig[Constants.effect]


    def activate(self,modifier,isCrit,text):
        return self.effect
