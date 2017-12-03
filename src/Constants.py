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

#action vocabulary
action = 'action'

trade = 'trade'

take = 'take'

give = 'give'

swing = 'swing'
stab = 'stab'
heal = 'heal'
fire = 'fire'

organized_action_vocab = {
    "item_use": {'character_interact': [give], 'item_interact': [swing, stab, heal, fire]},
    "non_item_use": {'character_interact': [trade], 'item_interact': [take]}
}