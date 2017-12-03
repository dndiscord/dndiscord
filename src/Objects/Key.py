from src.Objects.Item import Item
from src import Constants

class Key(Item):
    def __init__(self, object_config, door, room):
        super().__init__(object_config)
        self.room = room # room the key is in
        self.door = door # door the key opens

    def activate(self, user, isCrit):
        return {
            Constants.description: "{} used {} to {}".format(user.name, self.name, self.effect),
            Constants.attack: user.attack + self.attack,
            Constants.effect: self.effect,
            Constants.target: self.door
        }
