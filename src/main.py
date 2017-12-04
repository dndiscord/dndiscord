import copy
import os
import sys

import discord

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
sys.setrecursionlimit(10000)

from src.Objects.Item import Item
from src.Space import make_rooms
from src.Objects.Character import Character
from src.Data import GameStage
from src import Constants, Data
from src.GameLogic import CreateCharacter, CharacterAction, Restart, RoomChange, StatusReport, FightCycle

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def print_message(channel, to_print):
    await client.send_message(channel, to_print)


@client.event
async def on_message(message):
    if message.author.name == client.user.name:
        return
    if message.content.startswith(Constants.start):
        data.current_player = message.author.name
        await client.send_message(message.channel, 'Welcome to DnDiscord!\n{}, enter your player name:'.format(message.author.name))
        data.gamestage = Data.GameStage.CHARACTER_CREATE

    elif message.content.startswith('!credits'):
        await client.send_message(message.channel, 'Developed by Kristof, Noah, and Harley')

    elif data.gamestage == GameStage.CHARACTER_CREATE:
        await creator.getMessage(message)

    elif data.gamestage == GameStage.FIGHT:
        await fightCycle.getMessage(message, actionPrompt)

    elif message.content.startswith(Constants.restart):
        Restart.Restart.restart()

    elif message.content.startswith(Constants.fight):
        data.gamestage = GameStage.FIGHT
        await fightCycle.start_cycle(message)

    elif message.content.startswith(Constants.createCharacter):
        data.current_player = message.author.name
        await client.send_message(message.channel, '{}, Enter your player name:'.format(message.author.name))
        data.gamestage = Data.GameStage.CHARACTER_CREATE

    elif message.content.startswith(Constants.status):
        await statusPrompt.print_current_statuses(message)

    elif message.content.startswith(Constants.my_status):
        await statusPrompt.print_my_status(message)

    elif message.content.startswith(Constants.heroAction):
        await actionPrompt.do_action(message)

    elif message.content.startswith(Constants.partyAction):
        await roomChange.parse_action(message)

data = Data.Data({
    Constants.items: [],
    Constants.characters: [],
    Constants.rooms: copy.copy(Constants.room_names),
    Constants.doors: copy.copy(Constants.door_names),
})
data.current_room.objects.append(
    Character(
        {Constants.health: 500,
         Constants.value: 50,
         Constants.attack: 0,
         Constants.speed: 0,
         Constants.mana: 0,
         Constants.crit: 0,
         Constants.name: "Target_Dummy",
         Constants.description: "An unassuming target dummy",
         Constants.inventory: [Item({
                Constants.name: "Head",
                Constants.description: "The head of your conquered foe, the target dummy",
                Constants.value: 100,
                Constants.effect: "bludgeon",
                Constants.health: 200,
                Constants.attack: 20,
                Constants.inventory: []
            })]
         }
    ))
creator = CreateCharacter.CreateCharacter(print_message, data)
actionPrompt = CharacterAction.CharacterAction(print_message, data)
statusPrompt = StatusReport.StatusReport(print_message, data)
roomChange = RoomChange.RoomChange(print_message, data)
fightCycle = FightCycle.FightCycle(print_message, data)

#creator.assign_stats('elf', 'hunter', 'gg', 'chronular#4496')
#creator.assign_stats('troll', 'librarian', 'quaz', 'Quaznal#8096')
client.run(sys.argv[1])

