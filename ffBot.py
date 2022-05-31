import os
import discord
import asyncio
import aiohttp
import pyxivapi
import supportedConents

from dotenv import load_dotenv

load_dotenv()
DISC_TOKEN = os.getenv('DISCORD_TOKEN')
XIV_TOKEN = os.getenv('XIVAPI_TOKEN')

client = discord.Client()

@client.event
async def on_ready(): 
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot: # no infinite loops from bot response message
        return

    if message.content.startswith("!help"):
        channel = message.channel
        await channel.send("List of commands you can use: \n!raid [encounter name e.g. zodiark]\n!character [First name Last name]")

    if message.content.startswith("!raid"):
        encounter = str(message.content)[6:]
        channel = message.channel
        if not encounter: # no raid specified / empty after !raid
            await channel.send("Type raid name after !raid.\ne.g. !raid p4s")
        else:
            await channel.send(supportedConents.encounters[encounter])
    
    if message.content.startswith("!char"):
        name = str(message.content)[6:]
        channel = message.channel
        if not name: # no raid specified / empty after !raid
            await channel.send("Type character name and server name after !char.\ne.g. !char Ravi Lavi Leviathan")
        else:
            client = pyxivapi.XIVAPIClient(api_key=XIV_TOKEN)

            



client.run(DISC_TOKEN)
