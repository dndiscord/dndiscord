from enum import Enum

#Object config
crit = "crit"
name = "name"
attack = "attack"
description = "description"
value = "value"
speed = "speed"
mana = "mana"
activate = "activate"
effect = "effect"
health = "health"
inventory = "inventory"
user = 'user'

#Commands
restart = "!restart"
createCharacter = "!createCharacter"
heroAction = "!hero"
start = "!start"
partyAction = "!party"
status = '!status'
my_status = '!mystatus'

#Database categories
items = 'items'
rooms = 'rooms'
doors = 'doors'
characters = 'characters'

# room stuff
door_names = ["blue", "purple", "red", "green", "orange", "black", "white", "yellow", "huge", "cool", "skeleton", "Abloy", "invisible", "indivisible"]
room_names = ["big house", "town square", "garden", "dungeon", "supermarket", "town hall", "corner store", "small house", "abandoned cemetary", "haven", "park", "party", "factory", "storm drains", "janitor's closet"]

action_vocabulary = {
    "item_use": {'character_interact': [], 'item_interact': ['swing', 'stab', 'heal']},
    "non_item_use": {'character_interact': ['buy'], 'item_interact': ['grab']}
}