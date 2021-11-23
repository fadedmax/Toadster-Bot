import discord
from discord.ext import commands
import random
import art
import requests

class misc(commands.Cog):
    def __inti__(self, bot):
        self.bot=bot
         
    @commands.command()
    async def image(self, ctx, query):
        request=requests.get(f"https://source.unsplash.com/1600x900/?{query}")
        file=open("./assests/picture.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/picture.png"))

    @commands.command()
    async def jail(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request = requests.get(f"https://some-random-api.ml/canvas/jail?avatar={user.avatar_url_as(format='png')}")
        file=open("./assests/jailed.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/jailed.png"))    

    @commands.command()
    async def ascii(self, ctx, *, text):
        if len(text) > 15:
            return await ctx.reply("Message too long!")
        await ctx.reply(f"```\n{art.text2art(text)}\n```")

    @commands.command()
    async def art(self, ctx, query):
        try:
            await ctx.reply(f"```\n{art.art(query)}\n```")  
        except art.artError:
            await ctx.reply("Invalid art!")    

    @commands.command()
    async def passed(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author           
        request = requests.get(f"https://some-random-api.ml/canvas/passed?avatar={user.avatar_url_as(format='png')}")
        file=open("./assests/passed.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/passed.png"))   

    @commands.command()
    async def triggered(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request = requests.get(f"https://some-random-api.ml/canvas/triggered?avatar={user.avatar_url_as(format='png')}")
        file=open("./assests/triggered.gif", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/triggered.gif")) 

    @commands.command()
    async def comrade(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request=requests.get(f"https://some-random-api.ml/canvas/comrade?avatar={user.avatar_url_as(format='png')}")
        file=open("./assests/comrade.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/comrade.png"))   

    @commands.command()
    async def gay(self, ctx, user:discord.User=None):
        if user == None:
            user = ctx.author
        request = requests.get("https://some-random-api.ml/canvas/gay?avatar={}".format(user.avatar_url_as(format='png')))
        file = open("./assests/gay.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/gay.png"))        

    @commands.command()
    async def comment(self, ctx, user:discord.User, *, message):
        if user == discord.User:
            request = requests.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={user.avatar_url_as(format='png')}&username={user.name}&comment={message}")       

        file = open("./assests/tweet.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/tweet.png"))




def setup(bot):
    bot.add_cog(misc(bot))        
       