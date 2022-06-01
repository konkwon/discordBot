import os
import discord
import asyncio
import aiohttp
import pyxivapi
import supportedConents

from dotenv import load_dotenv

load_dotenv()
# keys encrypted using git crypt
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
        await channel.send("List of commands you can use: \n!raid [encounter name e.g. zodiark]\n!char [Character Name Server e.g. Ravi Lavi Leviathan]")

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
            inputs = name.split()
            jobLevel = {}
            i = 0

            char = await client.character_search(world = inputs[2] , forename = inputs[0] , surname = inputs[1])
            lode = await client.character_by_id(lodestone_id = char['Results'][0]['ID'] , extended = False , include_freecompany = False)

            for x in lode['Character']['ClassJobs']:
                if lode['Character']['ClassJobs'][i]['Level'] == 0:
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], ' - ')
                elif lode['Character']['ClassJobs'][i]['Level'] < 10:
                    level = '' + str(lode['Character']['ClassJobs'][i]['Level']) + ' '
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], level)
                else:
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], lode['Character']['ClassJobs'][i]['Level'])
                i += 1

            embedVar = discord.Embed(title = (char['Results'][0]['Name']), description = (char['Results'][0]['Server']), color=0x336666)
            embedVar.set_thumbnail(url = (char['Results'][0]['Avatar']))
            # Icons pulled from own private Discord server
            embedVar.add_field(
                            name="Jobs", 
                            value="<:pld:981415124562743296> " + " <:war:981415184688091146> "  + " <:drk:981417660115984474> "  + " <:gnb:981415094791589988> "  + '\n' +
                                  str(jobLevel[19]).ljust(3, "") + str(jobLevel[21]).ljust(3, "") + str(jobLevel[32]).ljust(3, "") + str(jobLevel[37]).ljust(3, "") + '\n' +
                                  "<:whm:981415191872942090> " + " <:sch:981415162433110026> "  + " <:ast:981414770215362661> " + " <:sge:981415169768972390> " + '\n' +
                                  str(jobLevel[24]).ljust(3, "") + str(jobLevel[28]).ljust(3, "") + str(jobLevel[33]).ljust(3, "") + str(jobLevel[40]).ljust(3, "") + '\n' +
                                  "<:mnk:981415109912064040> " + " <:drg:981415086319075339> " + " <:nin:981415116543262761> " + " <:sam:981415154086449162> " + " <:rpr:981415140115222538> " + '\n' +
                                  str(jobLevel[20]).ljust(3, "") + str(jobLevel[22]).ljust(3, "") + str(jobLevel[30]).ljust(3, "") + str(jobLevel[34]).ljust(3, "") + str(jobLevel[39]).ljust(3, "") + '\n' +
                                  "<:brd:981414794466844692> " + " <:mch:981415102702034964> " + " <:dnc:981414801743953920> " + '\n' +
                                  str(jobLevel[23]).ljust(3, "") + str(jobLevel[31]).ljust(3, "") + str(jobLevel[38]).ljust(3, "") + '\n' +
                                  "<:blm:981414778079707136> " + " <:smn:981415176790237245> " + " <:rdm:981415132372533248> " + " <:blu:981414786904490074> " + '\n' +
                                  str(jobLevel[25]).ljust(3, "") + str(jobLevel[27]).ljust(3, "") + str(jobLevel[35]).ljust(3, "") + str(jobLevel[36]).ljust(3, "") + '\n'
                                  , 
                            inline=True)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
            await message.channel.send(embed=embedVar)
            await client.session.close()




client.run(DISC_TOKEN)
