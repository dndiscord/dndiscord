from src.Objects.Item import Item
from src import Constants

class Key(Item):
    def __init__(self, door, room):
        super().__init__({
                Constants.name: door + "Key",
                Constants.description: "A key to the " + door + " door",
                Constants.value: 100,
                Constants.effect: "unlocked",
                Constants.health: 5,
                Constants.attack: 2,
                Constants.inventory: []
                })
        self.room = room # room the key is in
        self.door = door # door the key opens

    def activate(self, user, isCrit):
        return {
            Constants.description: "{} used {} to {}".format(user.name, self.name, self.effect),
            Constants.attack: self.attack,
            Constants.effect: self.effect,
            Constants.target: self.door
        }
