from src.Objects.Item import Item

class Key(Item):
    def __init__(self, exit):
        self.room = None # room the key is in
        self.exit = exit # exit the key opens

