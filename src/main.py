import sys
import discord
import asyncio

from src import Constants, Data
from src.GameLogic import CreateCharacter, CharacterAction, Restart

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def print_message(message):
    await client.send_message(message.channel, message)


@client.event
async def on_message(message):
    #TODO set up global gamestate enum, based on gamestate call in class receive methods.

    if message.content.startswith('!credits'):
        await client.send_message(message.channel, 'Developed by Kristof, Noah, and Harley')

    elif message.content.startswith(Constants.restart):
        Restart.Restart.restart()

    elif message.content.startswith(Constants.createCharacter):
        CreateCharacter.CreateCharacter(print_message,data)

    elif message.content.startswith(Constants.heroAction):
        actionPrompt = CharacterAction.CharacterAction(print_message,data)
        actionPrompt.do_action(message.content)

data = Data.Data({
    Constants.items: [],
    Constants.characters: [],
    Constants.rooms: []
})
client.run(sys.argv[1])
