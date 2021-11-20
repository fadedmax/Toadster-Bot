import discord
from discord.ext import commands
import requests
import json
import collections
import operator

import asyncio
class misc(commands.Cog):
    def __init__(self, bot):
        apikey = "lmWpIMRSRzZ0dJE5EFfV2p2gt"
        self.bot = bot
    @commands.command()
    async def screenshot(self, ctx, url):
        if "porn" or "p0rn" or "XXX" or "xxx" in url.lower():
            return
            await ctx.send("That is NSFW!")
        request = requests.get(f"https://image.thum.io/get/{url}")
        file = open("./assests/screenshot.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file=discord.File("./assests/screenshot.png"))
    @commands.command(aliases=['image', 'pic'])
    async def img(self, ctx, query):
        request = requests.get(f"https://source.unsplash.com/1600x900/?{query}")
        file = open("./assests/picture.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file=discord.File("./assests/picture.png"))
    @commands.command()
    async def jail(self, ctx, user:discord.User=None):
        if user == None:
         avatar = ctx.author.avatar_url_as(format='png')

        else:
            avatar=user.avatar_url_as(format='png')
        request= requests.get("https://some-random-api.ml/canvas/jail?avatar={}".format(avatar))
        file = open("./assests/jailed.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file=discord.File("./assests/jailed.png"))
    @commands.command()
    async def wasted(self, ctx, user:discord.User=None):
        if user == None:
            avatar = ctx.author.avatar_url_as(format='png')
        else:
            avatar = user.avatar_url_as(format='png')
        request = requests.get("https://some-random-api.ml/canvas/wasted?avatar={}".format(avatar))
        file = open("./assests/wasted.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file=discord.File("./assests/wasted.png"))
    @commands.command()
    async def gay(self, ctx, user:discord.User=None):
        if user == None:
            avatar = ctx.author.avatar_url_as(format="png")
        else:
            avatar = user.avatar_url_as(format="png")
        request = requests.get("https://some-random-api.ml/canvas/gay?avatar={}".format(avatar))
        file = open("./assests/gay.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file = discord.File("./assests/gay.png"))
    @commands.command()
    async def triggered(self, ctx, user:discord.User=None):
        if user == None:
            avatar = ctx.author.avatar_url_as(format="png")
        else:
            avatar = user.avatar_url_as(format="png")
        request = requests.get("https://some-random-api.ml/canvas/triggered?avatar={}".format(avatar))
        file = open("./assests/triggered.gif", "wb")
        file.write(request.content)
        file.close()
        await ctx.send(file=discord.File("./assests/triggered.gif"))

    @commands.command()
    async def rank(self, ctx, member:discord.User=None):
        if member == None:
         member=ctx.author
         with open("./dicts/levels.json", "r") as f:
            users = json.load(f, object_pairs_hook=collections.OrderedDict)
         xp = str(users[f'{ctx.guild.id}']['users'][f'{member.id}']['xp'])
         level = users[f'{ctx.guild.id}']['users'][f'{member.id}']['level']

         if int(xp) <= 999:
            xp = xp
         elif int(xp) in range(1000, 9999):
            xp = f"{str(xp[0])}.{str(xp[1])}K"
         elif int(xp) in range(10000, 99999):
            xp = f"{str(xp[0])}.{str(xp[1])}{str(xp[2])}K"
         else:
            xp = f"{str(xp[0])}.{str(xp[1])}{str(xp[2])}{str(xp[3])}K"



         level_dict = {0:255, 1:510, 2:1020, 3:2040, 4:4080, 5:8160, 6:"16,320", 7:"32,640", 8:"65,280", 9:"130,560", 10:"261,120"}
         request = requests.get(f"https://some-random-api.ml/premium/rankcard/1?key=lmWpIMRSRzZ0dJE5EFfV2p2gt&username={member.name}&discriminator={member.discriminator}&avatar={member.avatar_url_as(format='png')}&cxp={xp}&nxp={level_dict.get(users[f'{ctx.guild.id}']['users'][f'{member.id}']['level'])}&level={level}&cbg=3f3f3f&ctext=ffffff&ccxp=39d0fd&cbar=ffffff")
         file = open("./assests/rankcard.png", "wb")
         file.write(request.content)
         file.close()
         await ctx.send(file=discord.File("./assests/rankcard.png"))
        else:
            with open("./dicts/levels.json", "r") as f:
               users = json.load(f, object_pairs_hook=collections.OrderedDict)
            xp = str(users[f'{ctx.guild.id}']['users'][f'{member.id}']['xp'])
            level = users[f'{ctx.guild.id}']['users'][f'{member.id}']['level']

            if int(xp) <= 999:
               xp = xp
            elif int(xp) in range(1000, 9999):
               xp = f"{str(xp[0])}.{str(xp[1])}K"
            elif int(xp) in range(10000, 99999):
               xp = f"{str(xp[0])}.{str(xp[1])}{str(xp[2])}K"
            else:
               xp = f"{str(xp[0])}.{str(xp[1])}{str(xp[2])}{str(xp[3])}K"



            level_dict = {0:255, 1:510, 2:1020, 3:2040, 4:4080, 5:8160, 6:"16,320", 7:"32,640", 8:"65,280", 9:"130,560", 10:"261,120"}
            request = requests.get(f"https://some-random-api.ml/premium/rankcard/1?key={apikey}&username={member.name}&discriminator={member.discriminator}&avatar={member.avatar_url_as(format='png')}&cxp={xp}&nxp={level_dict.get(users['users'][f'{member.id}']['level'])}&level={level}&cbg=3f3f3f&ctext=ffffff&ccxp=39d0fd&cbar=ffffff")
            file = open("./assests/rankcard.png", "wb")
            file.write(request.content)
            file.close()
            await ctx.send(file=discord.File("./assests/rankcard.png"))
    @commands.command()
    async def nick(self, ctx, *, nick):
        await ctx.author.edit(nick=f"{nick}[{ctx.author}]")
        await ctx.reply(f"Changed your nickname to {nick}.")


def setup(bot):
    bot.add_cog(misc(bot))
