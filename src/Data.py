from src import Constants
from enum import Enum
import copy


class GameStage(Enum):
    CHARACTER_CREATE = 1 
    MOVE = 2 
    FIGHT = 3 


class Data:

    def __init__(self, game_start_data):
        self.items = game_start_data[Constants.items]
        self.rooms = game_start_data[Constants.rooms]
        self.characters = game_start_data[Constants.characters]
        self.current_scenario = game_start_data[Constants.current_scenario]
        self.exit_names = copy.copy(Constants.exit_names)
        self.gamestage = GameStage.CHARACTER_CREATE
        self.current_player = ""

    def add_character(self, character):
        self.characters.append(character)

    def get_character(self, name):
        return next(iter([c for c in self.characters if c.name == name] or []), None)

    def get_item(self, name):
        return next(iter([i for i in self.items if i.name == name] or []), None)

    def get_from_current_scenario(self,name):
        return next(iter([i for i in self.current_scenario if i.name == name]), None)
