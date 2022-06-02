import os
import discord
import asyncio
import aiohttp
import pyxivapi
import supportedConents
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from dotenv import load_dotenv

load_dotenv()
# keys encrypted using git crypt
DISC_TOKEN = os.getenv('DISCORD_TOKEN')
XIV_TOKEN = os.getenv('XIVAPI_TOKEN')

client = commands.Bot("!", help_command = None)
DiscordComponents(client)

@client.event
async def on_ready(): 
    print(f'{client.user} has connected to Discord!')

@client.command()
async def help(ctx):
    await ctx.send("List of commands you can use: \n!raid [encounter name e.g. zodiark]\n!char [Character Name Server e.g. Ravi Lavi Leviathan]")

@client.command()
async def raid(ctx, *arg):
    if not arg: # no raid specified / empty after !raid
        await ctx.send("Type raid name after !raid.\ne.g. !raid p4s")
    elif arg[0] in supportedConents.encounters:
        await ctx.send(supportedConents.encounters[arg[0]])
    else:
        await ctx.send("Not supported content. Currently supporting Extreme Trials and Savage contents from Shadowbringer and later.")

@client.command()
async def c(ctx, *arg):
    if not arg:
        await ctx.send("Type character name and server name after !char.\ne.g. !char Ravi Lavi Leviathan")
    elif len(arg) == 3:
        try:
            api = pyxivapi.XIVAPIClient(api_key=XIV_TOKEN)
            jobLevel = {}
            i = 0

            char = await api.character_search(world = arg[2] , forename = arg[0] , surname = arg[1])
            lode = await api.character_by_id(lodestone_id = char['Results'][0]['ID'] , extended = False , include_freecompany = False)

            for x in lode['Character']['ClassJobs']:
                if lode['Character']['ClassJobs'][i]['Level'] == 0:
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], ' - ')
                elif lode['Character']['ClassJobs'][i]['Level'] < 10:
                    level = '' + str(lode['Character']['ClassJobs'][i]['Level']) + ' '
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], level)
                else:
                    jobLevel.__setitem__(lode['Character']['ClassJobs'][i]['JobID'], lode['Character']['ClassJobs'][i]['Level'])
                i += 1

            page1 = discord.Embed(title = (char['Results'][0]['Name']), description = (char['Results'][0]['Server']), color=0x336666)
            page1.set_thumbnail(url = (char['Results'][0]['Avatar']))
            # Icons pulled from own private Discord server
            page1.add_field(
                            name="Jobs", 
                            value="<:pld:981415124562743296> " + " <:war:981415184688091146> "  + " <:drk:981417660115984474> "  + " <:gnb:981415094791589988> "  + '\n' +
                                    str(jobLevel[19]).ljust(4, "") + str(jobLevel[21]).ljust(4, "") + str(jobLevel[32]).ljust(4, "") + str(jobLevel[37]).ljust(4, "") + '\n' +
                                    "<:whm:981415191872942090> " + " <:sch:981415162433110026> "  + " <:ast:981414770215362661> " + " <:sge:981415169768972390> " + '\n' +
                                    str(jobLevel[24]).ljust(4, "") + str(jobLevel[28]).ljust(4, "") + str(jobLevel[33]).ljust(4, "") + str(jobLevel[40]).ljust(4, "") + '\n' +
                                    "<:mnk:981415109912064040> " + " <:drg:981415086319075339> " + " <:nin:981415116543262761> " + " <:sam:981415154086449162> " + " <:rpr:981415140115222538> " + '\n' +
                                    str(jobLevel[20]).ljust(4, "") + str(jobLevel[22]).ljust(4, "") + str(jobLevel[30]).ljust(4, "") + str(jobLevel[34]).ljust(4, "") + str(jobLevel[39]).ljust(4, "") + '\n' +
                                    "<:brd:981414794466844692> " + " <:mch:981415102702034964> " + " <:dnc:981414801743953920> " + '\n' +
                                    str(jobLevel[23]).ljust(4, "") + str(jobLevel[31]).ljust(4, "") + str(jobLevel[38]).ljust(4, "") + '\n' +
                                    "<:blm:981414778079707136> " + " <:smn:981415176790237245> " + " <:rdm:981415132372533248> " + " <:blu:981414786904490074> " + '\n' +
                                    str(jobLevel[25]).ljust(4, "") + str(jobLevel[27]).ljust(4, "") + str(jobLevel[35]).ljust(4, "") + str(jobLevel[36]).ljust(4, "") + '\n'
                                    , 
                            inline=True)

            page2 = discord.Embed(title = (char['Results'][0]['Name']), description = (char['Results'][0]['Server']), color=0x336666)
            page2.set_thumbnail(url = (char['Results'][0]['Avatar']))
            page2.add_field(
                            name="test", 
                            value="<:crp:981414565755637840> " + " <:bsm:981414520872394752> " + " <:arm:981414511326167091> " + " <:gsm:981414735322968095> " + '\n' +
                                    str(jobLevel[8]).ljust(4, "") + str(jobLevel[9]).ljust(4, "") + str(jobLevel[10]).ljust(4, "") + str(jobLevel[11]).ljust(4, "") + '\n' +
                                    "<:ltw:981414742700732438> " + " <:wvr:981414759356334091> " + " <:alc:981414453792894987> " + " <:cul:981414719128748092> " + '\n' +
                                    str(jobLevel[12]).ljust(4, "") + str(jobLevel[13]).ljust(4, "") + str(jobLevel[14]).ljust(4, "") + str(jobLevel[15]).ljust(4, "") + '\n' +
                                    "<:min:981414751332601887> " + " <:btn:981414531047784489> " + " <:fsh:981414727538319390> " + '\n' +
                                    str(jobLevel[16]).ljust(4, "") + str(jobLevel[17]).ljust(4, "") + str(jobLevel[18]).ljust(8, "") + '\n'
                                    ,
                            inline=True)

            pages = {"page1": page1, "page2": page2}

            await api.session.close()

            msg = await ctx.send(embed = page1, components = [[Button(label = '1', style = '2', custom_id = 'page1'), Button(label = '2', style = '2', custom_id = 'page2')]])
            while True:
                event = await client.wait_for("button_click")

                if event.channel is not ctx.channel:
                    return

                if event.channel == ctx.channel:
                    response = pages.get(event.component.id)
                    await msg.edit(embed=response)

                    if response is None:
                        await event.channel.send("error, try again.")
                
                await event.respond(type=6)
        except:
            await ctx.send("Couldn't find the character. Check again.")
            await api.session.close()
    else:
        await ctx.send("error")



client.run(DISC_TOKEN)
