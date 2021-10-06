import discord
import requests
import re
from discord.ext import commands
from bs4 import BeautifulSoup

token = "NzY2NTQ3MDE4NTk1NDM0NTM3.X4k8ig.tXHmuuSVXbyeZv6Ns-rZbqSFQws"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="delusional thoughts"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Patch notes
    if message.content.startswith('!patch'):
        url = "https://na.leagueoflegends.com/en-us/news/tags/patch-notes"
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        address = "https://na.leagueoflegends.com"
        address += soup.a["href"]

        index = address.index("patch")
        season = address[index + 6:index + 8]

        if index == 55:
            version = address[index + 9:index + 10]
        elif index == 56:
            version = address[index + 9:index + 11]

        patch = discord.Embed(
            title = "League of Legends " + season + "." + version + " Patch Note",
            url = address,
            colour = discord.Colour.teal()
        )

        patch.set_image(url="https://images.prismic.io/play-vs/13d11d702dbad5dca33f0e22abf4b3978381b5e7_league-of-legends-hero-splash.jpg?auto=compress,format")
        
        await message.channel.send(embed=patch)

    # High W/R builds/runes
    if message.content.startswith('!champion'):
        # Emoji link
        Lethal = "<:LethalTempoTemp:799466878598643722>"
        PTA = "<:PressTheAttack:799466878732337192>"
        Fleet = "<:FleetFootwork:799466878762221588>"
        Conqueror = "<:Conqueror:799430242082226196>"
        Electrocute = "<:Electrocute:799466878216831038>"
        DH = "<:DarkHarvest:799466878257856574>"
        Predator = "<:Predator:799466878627610644>"
        Hail = "<:HailOfBlades:799466878602313768>"
        Aery = "<:SummonAery:799466878607032390>"
        Comet = "<:ArcaneComet:799466878195990589>"
        Phase = "<:PhaseRush:799466878719492126>"
        Grasp = "<:GraspOfTheUndying:799466878606245898>"
        Aftershock = "<:VeteranAftershock:799466878727618560>"
        Guardian = "<:Guardian:799466878786863144>"
        Glacial = "<:GlacialAugment:799466878635737108>"
        Spellbook = "<:UnsealedSpellbook:799466878610702356>"
        Omnistone = "<:Omnistone:799466879038914620>"
        Overheal = "<:Overheal_rune:799466929232281610>"
        Triumph = "<:Triumph_rune:799466929038688257>"
        Presense = "<:Presence_of_Mind_rune:799466929248927745>"
        Cheap = "<:Cheap_Shot_rune:799466929013915689>"
        Taste = "<:Taste_of_Blood_rune:799466929177493524>"
        Sudden = "<:Sudden_Impact_rune:799466928816521228>"
        Nullify = "<:Nullifying_Orb_rune:799466929197678612>"
        Manaflow = "<:Manaflow_Band_rune:799466929244209162>"
        Cloak = "<:Nimbus_Cloak_rune:799466929332027392>"
        Demolish = "<:Demolish_rune:799466929186144286>"
        Font = "<:Font_of_Life_rune:799466929186144276>"
        Bash = "<:Shield_Bash_rune:799466929256398918>"
        Hextech = "<:Hextech_Flashtraption_rune:799466929189552178>"
        Boots = "<:Magical_Footwear_rune:799466929164779550>"
        Stopwatch = "<:Perfect_Timing_rune:799466928808525875>"
        Alacrity = "<:Legend_Alacrity_rune:799466946893578300>"
        Tenacity = "<:Legend_Tenacity_rune:799466947367927808>"
        Bloodline = "<:Legend_Bloodline_rune:799466946588180512>"
        Zombie = "<:Zombie_Ward_rune:799466946965536788>"
        Poro = "<:Ghost_Poro_rune:799466946974318652>"
        Eyeball = "<:Eyeball_Collection_rune:799466946965274644>"
        Trans = "<:Transcendence_rune:799466946990047242>"
        Celerity = "<:Celerity_rune:799466946936569906>"
        Absolute = "<:Absolute_Focus_rune:799466946889383946>"
        Conditioning = "<:Conditioning_rune:799466946885189652>"
        Wind = "<:Second_Wind_rune:799466946906685490>"
        Bone = "<:Bone_Plating_rune:799466946911141949>"
        Market = "<:Future27s_Market_rune:799466946889908304>"
        Minion = "<:Minion_Dematerializer_rune:799466946890301460>"
        Biscuit = "<:Biscuit_Delivery_rune:799466946617278557>"
        Coup = "<:Coup_de_Grace_rune:799467237831868473>"
        Cut = "<:Cut_Down_rune:799466968251236363>"
        Last = "<:Last_Stand_rune:799466968469209099>"
        Ravenous = "<:Ravenous_Hunter_rune:799467238683836426>"
        Ingenious = "<:Ingenious_Hunter_rune:799467237949833227>"
        Relentless = "<:Relentless_Hunter_rune:799466968587567145>"
        Ultimate = "<:Ultimate_Hunter_rune:799467238305300490>"
        Scorch = "<:Scorch_rune:799467124476477470>"
        Water = "<:Waterwalking_rune:799467238292979722>"
        Storm = "<:Gathering_Storm_rune:799467238423134269>"
        Overgrowth = "<:Overgrowth_rune:799467238078808095>"
        Revitalize = "<:Revitalize_rune:799467237924405259>"
        Unflinching = "<:Unflinching_rune:799467238272401458>"
        Cosmic = "<:Cosmic_Insight_rune:799537063976108082>"
        Velocity = "<:Approach_Velocity_rune:799537063920926801>"
        Tonic = "<:Time_Warp_Tonic_rune:799537063871250463>"

        name = message.content.replace(' ','')
        name = name[9:]
        name = name.capitalize()

        url = "https://u.gg/lol/champions/"+ name + "/build?rank=diamond_plus"
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # Champion Portrait
        portrait = str(soup.find("img", attrs={"class":"champion-image"}))
        index = portrait.find("src")
        portrait = portrait[index + 5:-3]

        # Champion Keystone
        keystone = str(soup.find("div", attrs={"class":"perk keystone perk-active"}))
        index1 = keystone.find("The Keystone")
        index2 = keystone.find('""')
        keystone = keystone[index1 + 13:index2 - 8]

        runetype = ""
        first = ""
        second = ""
        third = ""
        fourth = ""
        fifth = ""
        if keystone == "Lethal Tempo":
            keystone = Lethal
            runetype = "Precision"
        elif keystone == "Press the Attack":
            keystone = PTA
            runetype = "Precision"
        elif keystone == "Fleet Footwork":
            keystone = Fleet
            runetype = "Precision"
        elif keystone == "Conqueror":
            keystone = Conqueror
            runetype = "Precision"
        elif keystone == "Electrocute":
            keystone = Electrocute
            runetype = "Domination"
        elif keystone == "Dark Harvest":
            keystone = DH
            runetype = "Domination"
        elif keystone == "Predator":
            keystone = Predator
            runetype = "Domination"
        elif keystone == "Hail of Blades":
            keystone = Hail
            runetype = "Domination"
        elif keystone == "Summon Aery":
            keystone = Aery
            runetype = "Sorcery"
        elif keystone == "Arcane Comet":
            keystone = Comet
            runetype = "Sorcery"
        elif keystone == "Phase Rush":
            keystone = Phase  
            runetype = "Sorcery"
        elif keystone == "Grasp of the Undying":
            keystone = Grasp
            runetype = "Resolve"
        elif keystone == "Aftershock":
            keystone = Aftershock
            runetype = "Resolve"
        elif keystone == "Guardian":
            keystone = Guardian
            runetype = "Resolve"
        elif keystone == "Glacial Augment":
            keystone = Glacial
            runetype = "Inspiration"
        elif keystone == "Unsealed Spellbook":
            keystone = Spellbook
            runetype = "Inspiration"
        elif keystone == "Prototype: Omnistone":
            keystone = Omnistone
            runetype = "Inspiration"

        # Champion rest of runes
        perk_list = str(soup.find_all("div", attrs={"class":"perk perk-active"}))
        index1 = [m.start() for m in re.finditer("Rune", perk_list)]
        index2 = [n.start() for n in re.finditer('""', perk_list)]

        runes = [] * 5
        i = 0
        while (i < 5):
            runes.append(perk_list[index1[i] + 5: index2[i] - 8])
            i += 1

        # First row
        check = 0
        for i in runes:
            if i == "Overheal":
                if runetype == "Precision":
                    first = Overheal
                else:
                    fourth = Overheal
                    check = 1
            elif i == "Triumph":
                if runetype == "Precision":
                    first = Triumph
                else:
                    fourth = Triumph
                    check = 1
            elif i == "Presence of Mind":
                if runetype == "Precision":
                    first = Presense
                else:
                    fourth = Presense
                    check = 1
            elif i == "Cheap Shot":
                if runetype == "Domination":
                    first = Cheap
                else:
                    fourth = Cheap
                    check = 1
            elif i == "Taste of Blood":
                if runetype == "Domination":
                    first = Taste
                else:
                    fourth = Taste
                    check = 1
            elif i == "Sudden Impact":
                if runetype == "Domination":
                    first = Sudden
                else:
                    fourth = Sudden
                    check = 1
            elif i == "Nullifying Orb":
                if runetype == "Sorcery":
                    first = Nullify
                else:
                    fourth = Nullify
                    check = 1
            elif i == "Manaflow Band":
                if runetype == "Sorcery":
                    first = Manaflow
                else:
                    fourth = Manaflow
                    check = 1
            elif i == "Nimbus Cloak":
                if runetype == "Sorcery":
                    first = Cloak
                else:
                    fourth = Cloak
                    check = 1
            elif i == "Demolish":
                if runetype == "Resolve":
                    first = Demolish
                else:
                    fourth = Demolish
                    check = 1
            elif i == "Font of Life":
                if runetype == "Resolve":
                    first = Font
                else:
                    fourth = Font
                    check = 1
            elif i == "Shield Bash":
                if runetype == "Resolve":
                    first = Bash
                else:
                    fourth = Bash
                    check = 1
            elif i == "Hextech Flashtraption":
                if runetype == "Inspiration":
                    first = Hextech
                else:
                    fourth = Hextech
                    check = 1
            elif i == "Magical Footwear":
                if runetype == "Inspiration":
                    first = Boots
                else:
                    fourth = Boots
                    check = 1
            elif i == "Perfect Timing":
                if runetype == "Inspiration":
                    first = Stopwatch
                else:
                    fourth = Stopwatch
                    check = 1
            
            # Second row
            if i == "Legend: Alacrity":
                if runetype == "Precision":
                    second = Alacrity
                elif check == 0:
                    fourth = Alacrity
                else:
                    fifth = Alacrity
            if i == "Legend: Tenacity":
                if runetype == "Precision":
                    second = Tenacity
                elif check == 0:
                    fourth = Tenacity
                else:
                    fifth = Tenacity
            if i == "Legend: Bloodline":
                if runetype == "Precision":
                    second = Bloodline
                elif check == 0:
                    fourth = Bloodline
                else:
                    fifth = Bloodline
            if i == "Zombie Ward":
                if runetype == "Domination":
                    second = Zombie
                elif check == 0:
                    fourth = Zombie
                else:
                    fifth = Zombie
            if i == "Ghost Poro":
                if runetype == "Domination":
                    second = Poro
                elif check == 0:
                    fourth = Poro
                else:
                    fifth = Poro
            if i == "Eyeball Collection":
                if runetype == "Domination":
                    second = Eyeball
                elif check == 0:
                    fourth = Eyeball
                else:
                    fifth = Eyeball
            if i == "Transcendence":
                if runetype == "Sorcery":
                    second = Trans
                elif check == 0:
                    fourth = Trans
                else:
                    fifth = Trans
            if i == "Celerity":
                if runetype == "Sorcery":
                    second = Celerity
                elif check == 0:
                    fourth = Celerity
                else:
                    fifth = Celerity
            if i == "Absolute Focus":
                if runetype == "Sorcery":
                    second = Absolute
                elif check == 0:
                    fourth = Absolute
                else:
                    fifth = Absolute
            if i == "Conditioning":
                if runetype == "Resolve":
                    second = Conditioning
                elif check == 0:
                    fourth = Conditioning
                else:
                    fifth = Conditioning
            if i == "Second Wind":
                if runetype == "Resolve":
                    second = Wind
                elif check == 0:
                    fourth = Wind
                else:
                    fifth = Wind
            if i == "Bone Plating":
                if runetype == "Resolve":
                    second = Bone
                elif check == 0:
                    fourth = Bone
                else:
                    fifth = Bone
            if i == "Future's Market":
                if runetype == "Inspiration":
                    second = Market
                elif check == 0:
                    fourth = Market
                else:
                    fifth = Market
            if i == "Minion Dematerializer":
                if runetype == "Inspiration":
                    second = Minion
                elif check == 0:
                    fourth = Minion
                else:
                    fifth = Minion
            if i == "Biscuit Delivery":
                if runetype == "Inspiration":
                    second = Biscuit
                elif check == 0:
                    fourth = Biscuit
                else:
                    fifth = Biscuit

            # Third row
            if i == "Coup de Grace":
                if runetype == "Precision":
                    third = Coup
                else:
                    fifth = Coup
            if i == "Cut Down":
                if runetype == "Precision":
                    third = Cut
                else:
                    fifth = Cut
            if i == "Last Stand":
                if runetype == "Precision":
                    third = Last
                else:
                    fifth = Last
            if i == "Ravenous Hunter":
                if runetype == "Domination":
                    third = Ravenous
                else:
                    fifth = Ravenous
            if i == "Ingenious Hunter":
                if runetype == "Domination":
                    third = Ingenious
                else:
                    fifth = Ingenious
            if i == "Relentless Hunter":
                if runetype == "Domination":
                    third = Relentless
                else:
                    fifth = Relentless
            if i == "Ultimate Hunter":
                if runetype == "Domination":
                    third = Ultimate
                else:
                    fifth = Ultimate
            if i == "Scorch":
                if runetype == "Sorcery":
                    third = Scorch
                else:
                    fifth = Scorch
            if i == "Waterwalking":
                if runetype == "Sorcery":
                    third = Water
                else:
                    fifth = Water
            if i == "Gathering Storm":
                if runetype == "Sorcery":
                    third = Storm
                else:
                    fifth = Storm
            if i == "Overgrowth":
                if runetype == "Resolve":
                    third = Overgrowth
                else:
                    fifth = Overgrowth
            if i == "Revitalize":
                if runetype == "Resolve":
                    third = Revitalize
                else:
                    fifth = Revitalize
            if i == "Unflinching":
                if runetype == "Resolve":
                    third = Unflinching
                else:
                    fifth = Unflinching
            if i == "Cosmic Insight":
                if runetype == "Inspiration":
                    third = Cosmic
                else:
                    fifth = Cosmic
            if i == "Approach Velocity":
                if runetype == "Inspiration":
                    third = Velocity
                else:
                    fifth = Velocity
            if i == "Time Warp Tonic":
                if runetype == "Inspiration":
                    third = Tonic
                else:
                    fifth = Tonic

        champion = discord. Embed(
            title = name,
            colour = discord.Colour.teal()
        )

        champion.set_thumbnail(url = portrait)
        champion.add_field(
            name = "Runes",
            value = keystone + " " + fourth + "\n" 
                    "" + first + " " + fifth + "\n"
                    "" + second + "\n"
                    "" + third + "\n",

            inline = False)


        await message.channel.send(embed=champion)

    # Conversion
    if message.content.startswith('!convert'):        
        unit = message.content.replace(' ','')
        unit = unit[8:]

        number = re.findall(r"[-+]?\d*\.\d+|\d+", unit)

        unit = unit[len(str(number[0])):]
        if unit == "inch":
            conversion = round(float(number[0]) * 2.54, 4)
            final = str(conversion) + " cm"
        elif unit == "feet" or unit == "ft":
            conversion = round(float(number[0]) * 30.48, 4)
            final = str(conversion) + " cm"
        elif unit == "miles" or unit == "mile" or unit == "mi":
            conversion = round(float(number[0]) * 1.60934, 4)
            final = str(conversion) + " km"
        elif unit == "cm":
            conversion = round(float(number[0]) / 2.54, 2)
            feet = round(conversion / 12 , 2)
            final = str(conversion) + " inch or " + str(feet) + " feet"
        elif unit == "lb" or unit == "lbs":
            conversion = round(float(number[0]) / 2.205, 2)
            final = str(conversion) + " kg"
        elif unit == "kg":
            conversion = round(float(number[0]) * 2.205, 2)
            final = str(conversion) + " lbs"
        elif unit == "mph":
            conversion = round(float(number[0]) * 1.609, 1)
            final = str(conversion) + " kmh"
        elif unit == "kmh":
            conversion = round(float(number[0]) / 1.609, 1)
            final = str(conversion) + " mph"
        else:
            final = "Undesirable input, try again."
        
        await message.channel.send(final)

    # Random stuff
    if message.content.startswith('!hello'):
        await message.channel.send('Hey hey!')

client.run(token)
