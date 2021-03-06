from src import Constants
from src.Objects.Character import Character
from src.Space import make_rooms
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
        self.doors = game_start_data[Constants.doors]
        self.characters = game_start_data[Constants.characters]
        self.gamestage = GameStage.CHARACTER_CREATE
        self.current_player = ""
        self.current_room = make_rooms(self)

    def add_character(self, character):
        self.characters.append(character)

    def get_character_by_name(self, name):
        return next(iter([c for c in self.characters if c.name.lower() == name.lower()] or []), None)

    def get_character_by_user(self,user):
        return next(iter([c for c in self.characters if c.user.lower() == user.lower()] or []), None)

    def get_item(self, name):
        return next(iter([i for i in self.items if i.name.lower() == name.lower()] or []), None)

    def get_from_current_room(self,name):
        return next(iter([i for i in self.current_room.objects if i.name.lower() == name.lower()]), None)

    def get_player_characters_from_current_room(self):
        return [u for u in self.current_room.objects if isinstance(u,Character) and not u.is_npc()]

    def get_characters_from_current_room(self):
        return [c for c in self.current_room.objects if isinstance(c, Character)]

    def get_npcs_from_current_room(self):
        return [c for c in self.current_room.objects if isinstance(c, Character) and c.is_npc()]