from src import Constants


class Data:

    def __init__(self, game_start_data):
        self.items = game_start_data[Constants.items]
        self.rooms = game_start_data[Constants.rooms]
        self.characters = []

    def add_character(self,character):
        self.characters.append(character)

    def get_character(self, name):
        return [c for c in self.characters if c.name == name]

    def get_item(self, name):
        return [i for i in self.items if i.name == name]
