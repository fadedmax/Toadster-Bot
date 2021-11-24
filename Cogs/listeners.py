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
        if msg.author.bot:
            return
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


                
                

def setup(bot):
    bot.add_cog(listeners(bot))
