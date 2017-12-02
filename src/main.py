import sys
import discord
import asyncio
import os
import copy


lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
sys.setrecursionlimit(10000)

from src.Data import GameStage
from src import Constants, Data
from src.GameLogic import CreateCharacter, CharacterAction, Restart, RoomChange
from src.space import Room, generate

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
    #TODO set up global gamestate enum, based on gamestate call in class receive methods.
    
    if message.content.startswith('!credits'):
        await client.send_message(message.channel, 'Developed by Kristof, Noah, and Harley')
    
    elif data.gamestage == GameStage.CHARACTER_CREATE:
        creator = CreateCharacter.CreateCharacter(print_message, data)
        creator.getMessage(message)

    elif message.content.startswith(Constants.restart):
        Restart.Restart.restart()

    elif message.content.startswith(Constants.createCharacter):
        CreateCharacter.CreateCharacter(print_message, data)

    elif message.content.startswith(Constants.heroAction):
        actionPrompt = CharacterAction.CharacterAction(print_message, data)
        await actionPrompt.do_action(message)

    elif message.content.startswith(Constants.partyAction):
        roomChange = RoomChange.RoomChange(print_message, data)

data = Data.Data({
    Constants.items: [],
    Constants.characters: [],
    Constants.rooms: copy.copy(Constants.room_names),
    Constants.current_scenario: []
})
room = Room(data)
room.populate()
#generate(len(Constants.exit_names), 0, room, room)
room.show()
client.run(sys.argv[1])
