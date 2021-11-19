import discord
from discord.ext import commands, tasks
import json
import random
import collections


class listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        global userleveldict
        userleveldict = []

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        with open("./dicts/deleted_messages.json", "r") as f:
            load = json.load(f)

            dict = {f"message":{"content":f"{msg.content}", "author":f"{msg.author}"}}
            load.append(dict)
            with open("./dicts/deleted_messages.json", "w") as f2:
                json.dump(load, f2)

    @commands.Cog.listener()
    async def on_join(self, member):
        if f"{msg.author.id}" not in users['users']:
            users['users'][member.id] = {"level":0, "xp":0}
            print(f"Added user {member} to level list")
            with open("./dicts/levels.json", "w") as f2:
                json.dump(users, f2)
        else:
            return
    @commands.Cog.listener()
    async def on_message(self, msg):
        with open("./dicts/levels.json", "r") as f:
            users=json.load(f, object_pairs_hook=collections.OrderedDict)
        if f"{msg.author.id}" not in users['users']:
            users['users'][f"{msg.author.id}"] = {"level":0, "xp":0, "username":f"{msg.author}"}
            print(f"Added user {msg.author} to level list")
            with open("./dicts/levels.json", "w") as f2:
                json.dump(users, f2)


        else:
            xp = users['users'][f"{msg.author.id}"]['xp']
            level=users['users'][f"{msg.author.id}"]['level']
            level_1 = discord.utils.get(msg.guild.roles, name="Level 1")
            level_5 = discord.utils.get(msg.guild.roles, name="Level 5")
            level_10 = discord.utils.get(msg.guild.roles, name="Level 10")

            users['users'][f"{msg.author.id}"]['xp'] += random.choice([5, 10, 15, 20])

            if xp == 255 and level == 0:
                users['users'][f"{msg.author.id}"]['level'] = 1
                users['users'][f'{msg.author.id}']['xp'] = 0
                await msg.channel.send(f"{msg.author.mention} You are now level 1!")
                await msg.author.add_roles(level_1)
            elif xp == 510 and level == 1:
                users['users'][f"{msg.author.id}"]['level'] = 2
                users['users'][f'{msg.author.id}']['xp'] = 0
                await msg.channel.send(f"{msg.author.mention} You are now level 2!")
            elif xp == 1020 and level == 2:
                users['users'][f"{msg.author.id}"]['level'] = 3
                users['users'][f'{msg.author.id}']['xp'] = 0
                await msg.channel.send(f"{msg.author.mention} You are now level 3!")
            elif xp == 2040 and level == 3:
                users['users'][f"{msg.author.id}"]['level'] = 4
                users['users'][f'{msg.author.id}']['xp'] = 0
                await msg.channel.send(f"{msg.author.mention} You are now level 4!")
            elif xp == 4080 and level == 4:
                users['users'][f"{msg.author.id}"]['level'] = 5
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 5!")
                await msg.author.add_roles(level_5)
            elif xp == 8160 and level == 5:
                users['users'][f"{msg.author.id}"]['level'] = 6
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 6!")
            elif xp == 16320 and level == 6:
                users['users'][f"{msg.author.id}"]['level'] = 7
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 7!")
            elif xp == 32640 and level == 7:
                users['users'][f"{msg.author.id}"]['level'] = 8
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 8!")
            elif xp == 65280 and level == 8:
                users['users'][f"{msg.author.id}"]['level'] = 9
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 9!")
            elif xp == 130560 and level == 9:
                users['users'][f"{msg.author.id}"]['level'] = 10
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 10!")
                await msg.author.add_roles(level_10)
            elif xp == 261120 and level == 10:
                users['users'][f"{msg.author.id}"]['level'] = 11
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 11!")
            elif xp == 522240 and level == 11:
                users['users'][f"{msg.author.id}"]['level'] = 12
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 12!")
            elif xp == 1044480 and level == 12:
                users['users'][f"{msg.author.id}"]['level'] = 13
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 13!")
            elif xp == 2088960 and level == 13:
                users['users'][f"{msg.author.id}"]['level'] = 14
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 14!")
            elif xp == 4177920 and level == 14:
                users['users'][f"{msg.author.id}"]['level'] = 15
                users['users'][f'{msg.author.id}']['xp'] =0
                await msg.channel.send(f"{msg.author.mention} You are now level 15!")

            with open("./dicts/levels.json", "w") as f2:
                json.dump(users, f2)

def setup(bot):
    bot.add_cog(listeners(bot))
