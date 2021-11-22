import discord
from discord.ext import commands
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
        request = requests.get(f"https://some-random-api.ml/canvas/jail?avatar={ctx.author.avatar_url(format='png')}")
        file=open("./assests/jailed.png", "wb")
        file.write(request.content)
        file.close()
        await ctx.reply(file=discord.File("./assests/jailed.png"))    

    @commands.command()
    async def ascii(self, ctx, *, text):
        if len(text) > 14:
            return await ctx.reply("Message too long!") 
               


def setup(bot):
    bot.add_cog(misc(bot))        
       