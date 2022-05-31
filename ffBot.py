import os
import discord
import supportedConents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready(): 
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot: # no infinite loops from bot message
        return

    if message.content.startswith("!help"):
        channel = message.channel
        await channel.send("List of commands you can use: \n !raid \n !character")

    if message.content.startswith("!raid"):
        reply = str(message.content)[6:]
        channel = message.channel
        if not reply: # no raid specified / empty after !raid
            await channel.send("Type raid name after !raid. e.g. !raid p4s")
        else:
            await channel.send(supportedConents.encounters[reply])



client.run(TOKEN)
