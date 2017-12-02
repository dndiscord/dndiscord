from src.Objects.Item import Item

class Key(Item):
    def __init__(self, exit, room):
        self.room = room # room the key is in
        self.exit = exit # exit the key opens

