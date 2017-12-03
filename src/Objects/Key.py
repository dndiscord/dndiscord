from src.Objects.Item import Item
from src import Constants

class Key(Item):
    def __init__(self, object_config, room):
        super().__init__(object_config)
        self.room = room # room the key is in
        self.door = object_config[Constants.name] # door the key opens

