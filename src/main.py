import sys
import discord
import asyncio

from src import Constants
from src.GameLogic import CreateCharacter
from src.GameLogic import Restart

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #TODO set up global gamestate enum, based on gamestate call in class receive methods.

    if message.content.startswith('!credits'):
        await client.send_message(message.channel, 'Developed by Kristof, Noah, and Harley')

    elif message.content.startswith(Constants.restart):
        Restart.restart()

    elif message.content.startswith(Constants.createCharacter):
        CreateCharacter.CreateCharacter(message.channel)


client.run(sys.argv[1])
