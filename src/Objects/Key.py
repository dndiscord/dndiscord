from src.Objects.Item import Item

class Key(Item):
    def __init__(self, door, room):
        self.room = room # room the key is in
        self.door = door # door the key opens

